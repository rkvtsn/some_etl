import base64
import uuid
from decimal import Decimal
import time

import pandas as pd
import numpy as np

import conv
from config import load_settings

def to_number(column, is_int=None):
    """
    Parse and convert pandas.Series to int or float series
    :param column:
    :type column: pandas.Series
    :param is_int: is strictly integer
    :type is_int: bool
    :return:
    """
    return column.apply(conv.str_to_number, is_int=is_int)


# todo: make simpler
def transformation_mapping(service_name, source, file_name="mapping.json"):
    """
    Transformation mapping
    :param service_name:
    :type service_name: str
    :param source:
    :type source: dict
    :return:
    """
    result = {}
    target = {}
    _mapping = load_settings(file_name)

    if not service_name in _mapping:
        raise Exception("Wrong DB name in mapping configuration: %s" % service_name)

    # for batch in _mapping[service_name]:
    #     for target_tab, target_tab_values in batch.items():
    #         target_tab_name, target_col_name = target_tab.split('.')
    #         if not target.has_key(target_tab_name):
    #             target[target_tab_name] = pd.DataFrame([])
    #         for src_tab, src_col_value in target_tab_values.items():
    #             src_tab_name, src_col_name = src_tab.split('.')
    #             source[src_tab_name].columns = [x.lower() for x in source[src_tab_name].columns]
    #             if src_col_value is None or not isinstance(src_col_value, basestring):
    #                 target[target_tab_name][target_col_name] = src_col_value
    #             elif src_col_value == 'value':
    #                 target[target_tab_name][target_col_name] = source[src_tab_name].get(src_col_name)
    #             elif isinstance(src_col_value, dict) and src_col_value.has_key('expression'):
    #                 for index, expr in src_col_value['expression'].items():
    #                     if not source.has_key(src_tab_name):
    #                         raise Exception('Wrong mapping configuration, probably Source.')
    #                     column = source[src_tab_name].get(src_col_name)
    #                     x = source[src_tab_name]
    #                     y = target[target_tab_name]
    #                     target[target_tab_name][target_col_name] = eval(expr)
    #     if not result.has_key(target_tab_name):
    #         result[target_tab_name] = pd.DataFrame([])
    #     result[target_tab_name] = result[target_tab_name].append(target[target_tab_name])
    # return result

    for batch in _mapping[service_name]:
        for target_tab, target_tab_values in batch.items():
            target_tab_name, target_col_name = target_tab.split('.')
            if not target_tab_name in target:
                target[target_tab_name] = pd.DataFrame([])
            if isinstance(target_tab_values, dict):
                if 'value' in target_tab_values:
                    target[target_tab_name][target_col_name] = target_tab_values['value']
                elif 'field' in target_tab_values:
                    src_tab_name, src_col_name = target_tab_values['field'].split('.')
                    target[target_tab_name][target_col_name] = source[src_tab_name].get(src_col_name)
                elif 'expression' in target_tab_values:
                    x = source
                    y = target
                    for expr in  target_tab_values['expression']:
                        target[target_tab_name][target_col_name] = eval(expr)
                else:
                    raise Exception('Missing required fields in settings file')
            else:
                src_tab_name, src_col_name = target_tab_values.split('.')

                if target_col_name == 'unique':
                    target[target_tab_name]['unique'] = src_col_name + source[src_tab_name][src_col_name].astype(str)

                target[target_tab_name][target_col_name] = source[src_tab_name].get(src_col_name)

        if not target_tab_name in result:
            result[target_tab_name] = pd.DataFrame([])

        result[target_tab_name] = result[target_tab_name].append(target[target_tab_name])


    return result

#
# if target_tab_values.has_key('unique'):
#     unique_tab_name, unique_col_name = target_tab_values['unique'].split('.')
#
#     target[target_tab_name]['unique'] = target[target_tab_name][].astype(str) + target_tab_name
# el

def extraction_mapping(mapping_settings, fn):
    """
    Description of settings for extraction mapping
    Example:
    {
        "source_table_name": {
            "body": <request.body>,
            "headers": {
                "header": <request.header>,...
            },
        },...
    }
    :param mapping_settings:
    :param fn:
    :type fn: callable
    :return: Dictionary with source_table_name:request as key:value
    :rtype: dict
    """
    if not isinstance(mapping_settings, dict) or len(mapping_settings) == 0:
        raise ValueError('"mapping_settings" must be a not empty dict')

    if not callable(fn):
        raise ValueError('"fn" must be callable')

    source = {}
    for table_name, v in mapping_settings.items():
        source[table_name] = fn(**v)

    return source


if __name__ == "__main__":

    df_1 = conv.any_to_df([
        {"Name": "John_10", "Age": 10, "id": 1},
        {"Name": "Mike_20", "Age": 20, "id": 2},
        {"Name": "Phillip_30", "Age": 30, "id": 3},
    ])

    df_2 = conv.any_to_df([
        {"Name": "John_12", "Age": 12},
        {"Name": "Mike_22", "Age": 2},
        {"Name": "Phillip_32", "Age": 32},
    ])
    df_2['id'] = np.array(range(3, 6))

    df_3 = conv.any_to_df([
        {"name": "John", "Age": 3},
        {"name": "Mike", "Age": 53},
        {"name": "Phillip", "Age": 0},
    ])
    df_3['id'] = np.array(range(6, 9))
    df_4 = conv.any_to_df([
        {"Fullname": "JohnSmith", "A": 10},
        {"Fullname": "MikeDoe", "A": 20},
        {"Fullname": "PhillipLauren", "A": 30},
    ])
    df_4['id'] = np.array(range(9, 12))

    print transformation_mapping("radient",
                                 {"persons_1": df_1,
                                  "persons_2": df_2,
                                  "persons_3": df_3,
                                  "persons_4": df_4},
                                  "etl.json")['target']

    pass