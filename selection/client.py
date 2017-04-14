'''
Base class for Clients
'''
#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from contextlib import contextmanager
import abc


class Client:
    '''
    Base class for Clients
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError("Not implemented method")

    @abc.abstractmethod
    def connect(self):
        raise NotImplemented("Not implemented method")

    @abc.abstractmethod
    def __init__(self, connection_string):
        '''
        Constructor
        '''
        self.__connection_string = connection_string

    @property
    def connection_string(self):
        '''
        return connection string
        '''
        return self.__connection_string

    @abc.abstractmethod
    def request(self, body, **kwargs):
        '''
        Make a request and then return a response
        :param data: message body
        :type data: object
        :param headers: message headers
        :type headers: dict
        :return: result, status code
        :rtype: tuple
        '''
        pass

    @abc.abstractmethod
    def check_connection(self):
        '''
        Check connection to a Server
        :return: result of connection
        :rtype: bool
        '''
        return False

