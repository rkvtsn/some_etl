#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import json
import xml.etree.ElementTree as ET

import pandas as pd

from google.protobuf.message import Message
from protobuf_to_dict import protobuf_to_dict

## TODO REFACTORING


def xml_to_json(xml):
    """
    Convert XML string to JSON object (clear)
    :param xml: XML string
    :return: JSON object
    """
    return json.dumps(xml_to_dict_by_attrib(xml))


def xml_to_df(xml, encoding='UTF-8', by_attributes=True):
    """
    Convert XML string to Pandas.DataFrame object (clear)

    :param xml: an XML string
    :param encoding: set encoding (default: 'UTF-8')
    :param by_attributes: check attributes as columns (True)
    :return: DataFrame object
    """
    root = ET.fromstring(xml, parser=ET.XMLParser(target=ET.TreeBuilder(), encoding=encoding))

    titles = set()
    rows = []

    if by_attributes:
        for child in root:
            rows.append(child.attrib)
        return pd.DataFrame(rows)

    # online stuff
    for child in root:
        row = []
        for sub_child in child:
            row.append(sub_child.text)
            titles.add(sub_child.tag)
        rows.append(row)

    return pd.DataFrame(rows, columns=titles)


def xml_to_dict_by_attrib(xml, encoding=None):
    """
    Convert an XML string to the dictionary object
    :param xml: an XML string
    :type xml: str
    :return: dictionary
    :rtype: dict
    """
    if encoding is None:
        encoding = 'UTF-8'

    try:
        root = ET.fromstring(xml,
                             parser=ET.XMLParser(target=ET.TreeBuilder(), encoding=encoding))
    except Exception as err:
        print err
        return None

    rows = []

    for child in root:
        rows.append(child.attrib)

    return rows


def any_to_dict(raw, encoding=None):
    """
    Convert structured str to list of dict
    Implemented types: xml, protobuf2.4
    Returns None if unknown type.
    :param raw: string with data
    :type raw: str
    :param encoding: encoding of raw string
    :type encoding: str
    :return: serialized data to dictionary
    :rtype: dict
    """
    if isinstance(raw, Message):
        print "protobuf"
        return protobuf_to_dict(raw)['values']
    else:
        return xml_to_dict_by_attrib(raw, encoding)


def any_to_df(raw, **kwargs):
    """
    Convert a structured str to the pandas.DataFrame
    Implemented types: xml, protobuf2.4
    Returns None if unknown type.
    :param raw: raw data
    :param kwargs: implemented only 'encoding', default: None ('UTF-8')
    :type str:
    :return: serialized data to pandas.DataFrame
    :rtype: pandas.DataFrame
    """
    if not isinstance(raw, list):
        d = any_to_dict(raw, kwargs.get('encoding'))
        if d is None:
            return None
    else:
        d = raw
    df = pd.DataFrame(d)
    df.columns = [x.lower() for x in df.columns]
    return df


def str_to_number(s, is_int=False):
    """
    Parse a string to int or float
    :param s: string
    :param is_int: strict integer as a result or 0
    :return: number (float/int/) default 0
    """
    number = 0
    try:
        s = s.replace(',', '.')
        if s.find('.') != -1:
            number = float(s)
            if is_int == True:
                number = int(number)
        else:
            number = int(s)
    finally:
        return number
