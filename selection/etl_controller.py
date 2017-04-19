#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import abc
import pandas as pd
import time

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from client import Client
from util import mapper, conv


class EtlController(object):
    """
    """
    __metaclass__ = abc.ABCMeta

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, *args):
        self._disconnect()

    def _connect(self):
        self._client.connect()

    def _disconnect(self):
        self._client.disconnect()

    @abc.abstractproperty
    @property
    def service_name(self):
        """
        :return: name of source service (radient/integration)
        :rtype: str
        """
        raise NotImplementedError("Not implemented method")

    @abc.abstractmethod
    def _default_client(self):
        pass

    def __init__(self, selection_engine=None, client=None):
        """
        :param selection_engine: SQLAlchemy engine for Selection DB
        :type selection_engine: sqlalchemy.engine.interface.Connectable
        :param client: Client for transmission (client-server)
        :type client: Client
        """
        self._foreign_col_name = "foreign"
        self._unique_col_name = "unique"
        self._target_result = {}
        self._target = {}
        self.source = {}
        self.target = {}
        self.selection_engine = selection_engine
        if selection_engine is None:
            self.selection_engine = create_engine('postgresql://postgres:12345678@localhost:5432/mydatabase')
        self._selection = sessionmaker(bind=self.selection_engine)

        if client is None:
            client = self._default_client()
        self._client = client

    def check_connection(self):
        return self._client.check_connection()

    def request(self, body, **kwargs):
        return self._client.request(body, **kwargs)

    def _download(self, **kwargs):
        response, status = self.request(**kwargs)
        if status not in (200, 201):
            raise Exception("Bad response status: %s" % response)
        return conv.any_to_df(response, **kwargs)

    @abc.abstractmethod
    def source_mapping(self):
        """
        Description of settings for extraction mapping
        Example:
        {
            "source_table_name": {
                "body": <request.body>,
                "headers": {
                    "header": <request.header>,...
                }
            },...
        }
        :return: Dictionary with source_table_name:request as key:value
        :rtype: dict
        """
        pass

    def extract(self):
        """
        Extract all data in accordance with extraction mapping settings
        Example of result:
        {
            "source_table_name_1": <pandas.DataFrame>,
            "source_table_name_2": <pandas.DataFrame>
        }
        :return: Dictionary with source_table_name:pandas.DataFrames as key:value
        :rtype: dict
        """
        fn = self._download

        if not isinstance(self.source_mapping(), dict):
            raise ValueError('"mapping_settings" must be dict')
        if not callable(fn):
            raise ValueError('"fn" must be callable')

        for table_name, kwargs in self.source_mapping().viewitems():
            self.source[table_name] = fn(**kwargs)
        return self.source

    @abc.abstractmethod
    def transform(self):
        """
        Some example:
            self.init_target('table_name', 'id')
            self.get_target('table_name')['col_name'] = self.source['table_name']['col_name'] + 1
            self.merge_target()
            target = self.init_target('table_name', 'id')
            target['col_name'] = self.source['table_name']['col_name'] * 2
            self.merge_target()

        """
        raise NotImplementedError("Not implemented method")

    def get_target(self, table_name):
        # if table_name not in self._target:
        #     self._target[table_name] = pd.DataFrame([])
        return self._target[table_name]

    def init_target(self, table_name, col_name, **kwargs):
        self._target[table_name] = pd.DataFrame([])
        self._target[table_name][self._unique_col_name] = self.source[table_name][col_name]
        if 'foreign_table' in kwargs and 'foreign_col' in kwargs:
            foreign_table = kwargs['foreign_table']
            foreign_col = kwargs['foreign_col']
            self._target[table_name][self._foreign_col_name] = self.source[table_name][foreign_col] + foreign_table
        return self._target[table_name]

    def merge_target(self):
        for k, v in self._target.items():
            if k not in self._target_result:
                self._target_result[k] = v
            else:
                self._target_result[k].append(v)
        self._target = {}
        return self._target_result

    @abc.abstractmethod
    def load(self):
        """
        Load data to target DB
        :return:
        """
        #
        raise NotImplementedError("Not implemented method.")

    def sync(self):
        """
        """
        for tab_name, df in self._target_result.items():
            self._sync(table_name=tab_name, df=df)

    def _sync(self, table_name, df):
        """
        """
        index_col = self._unique_col_name
        if index_col not in df:
            raise Exception("DataFrame is bad: no unique column in table '%s'" % table_name)

        indexes = str(tuple(df[index_col]))
        sql_select = "SELECT * FROM {table_name} WHERE {index_col} IN {indexes}".format(table_name=table_name,
                                                                                        index_col=index_col,
                                                                                        indexes=indexes)
        try:
            db = pd.read_sql(sql_select, self.selection_engine)
        except:
            df.to_sql(table_name, self.selection_engine, index=False)
            sql_after_create = "ALTER TABLE {table_name} ADD PRIMARY KEY ({index_col})".format(table_name=table_name,
                                                                                         index_col=index_col)
            with self.selection_engine.begin() as conn:
                conn.execute(sql_after_create)
            return df
        df_new = df[~df.isin(db.to_dict('list')).all(1)]
        if not df_new.empty:
            sql_insert_or_update = self.get_sql_insert_or_update(table_name, df_new, index_col)
            self.save_sql(sql_insert_or_update, "sql_insert_or_update")
            with self.selection_engine.begin() as conn:
                conn.execute(sql_insert_or_update)
        return df_new

    # todo: move to other module
    def save_sql(self, sql, name):
        # with self.selection_engine.begin() as conn:
        #     conn.execute("INSERT INTO queries (query, table_name, t) VALUES (:sql, :name, NOW())",
        #                  name=name, sql=sql)
        with open('%s_%s.sql' % (name, int(time.time())), 'w') as f:
            f.write(sql)

    def get_sql_insert_or_update(self, table_name, df_new, index_col):
        sql_columns = str(tuple(df_new.columns)).replace("'", '')
        sql_values = ", ".join(str(tuple(x[1:])) for x in df_new.itertuples())
        sql_where = ", ".join("{col} = excluded.{col}".format(col=col) for col in df_new)

        sql_insert_or_update = "INSERT INTO {table_name} {sql_columns} " \
                               "VALUES {sql_values} " \
                               "ON CONFLICT ({index_col}) " \
                               "DO UPDATE SET {sql_where} " \
                               "RETURNING {index_col}".format(sql_columns=sql_columns,
                                                              table_name=table_name,
                                                              index_col=index_col,
                                                              sql_values=sql_values,
                                                              sql_where=sql_where)
        return sql_insert_or_update
