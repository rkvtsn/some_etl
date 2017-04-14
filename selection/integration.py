#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import uuid
import socket
import time

from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp

from client import Client
from proto import CommonProtos


class IntegrationClient(Client):

    def disconnect(self):
        self.logout()

    def connect(self):
        self.login(self._username, self._password)

    def request(self, data,**kwargs):
        print kwargs['java_class']
        send_to = kwargs.get('send_to', '/queue/test')
        reply_to = kwargs.get('reply_to', '/queue/test1')
        headers = kwargs.get('headers', {})

        # create Stomp client
        client = Stomp(StompConfig(self.connection_string))
        client.connect()

        # create message
        message = data.SerializeToString()

        if self.__sessionId is not None:
            headers['sessionId'] = self.__sessionId
            print headers['sessionId']

        corr_id = str(uuid.uuid4())
        content_length = len(message)
        message_id = str(uuid.uuid4())
        timestamp = str(int(time.time()))
        _headers = {
            'content-length': content_length,
            'messageId': message_id,
            'fromPK': 'test',
            'fromPM': 'test',
            'sessionId': message_id,
            'toPK': '',
            'toRm': '',
            'errorMsg': '',
            'timestamp': timestamp,
            'user': 'vasja',
            'correlation-id': corr_id,
            'reply-to': reply_to
        }
        _headers['classname'] = kwargs.get('java_class', '')

        # set rest of headers
        for k, v in headers.iteritems():
            _headers[k] = v

        # send & subscribe
        client.send(send_to, message, headers=_headers)

        if kwargs.get('with_response', True):
            client.subscribe(reply_to,
                             headers={StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL,
                                      "correlation-id": corr_id, "messageId": _headers['messageId']
                                      })
            frame = None
            body = None
            headers = {}
            try:
                frame = client.receiveFrame()
                client.ack(frame)
                body = frame.body
                headers = frame.headers
                if kwargs.has_key('proto_response'):
                    response_instance = kwargs['proto_response']()
                    response_instance.ParseFromString(frame.body)
                    return response_instance, headers
            except Exception as e:
                print e
                print "[request error] Aborted, please check your request."
            finally:
                client.disconnect()
            return body, headers

    def check_connection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # parse connection string
            begin = self.connection_string.find('://')
            if begin > 0: begin += 3
            address = self.connection_string[begin:].split(':')

            # convert port to integer
            address[1] = int(address[1])

            # try to connect
            s.connect(tuple(address))
        except Exception as err:
            print "[connection failed]: %s" % err
            return False

        return True

    def logout(self):
        logout_request = CommonProtos.LogoutRequest()
        logout_request.sessionId = self.__sessionId

        self.request(data=logout_request,
                     java_class="ru.nicetu.integration.messages.CommonProtos$LogoutRequest",
                     with_response=False)

        self.__sessionId = None
        pass

    def login(self, username, password):
        login_request = CommonProtos.LoginRequest()
        login_request.username = username
        login_request.password = password
        login_request.clientVersion = ""
        login_request.subscriber = "selection"
        login_request.clientTime = int(time.time())
        login_request.ip.append(socket.gethostbyname(socket.gethostname()))
        login_request.pkName = "test"
        login_request.hostName = "vasja"

        body, header = self.request(data=login_request,
                                    java_class="ru.nicetu.integration.messages.CommonProtos$LoginRequest")

        login_response = CommonProtos.LoginResponse()
        login_response.ParseFromString(body)

        try:
            self.__sessionId = login_response.sessionId
        except:
            print 'Error with sessionId'
            self.__sessionId = None
        finally:
            return self.is_auth()

    # todo Под вопросом! Постоянно вылетает
    @staticmethod
    def get_java_class(proto_obj, java_namespace="ru.nicetu.integration.messages", postfix='_pb2'):
        return java_namespace + proto_obj.__module__.replace("selection.proto", "").replace(postfix, "$") + proto_obj.__name__

    def __init__(self, connection_string, username, password):
        '''
        Init client and login
        :param connection_string: Connection string to service
        :type connection_string: str
        :param username: Username
        :type username: str
        :param password: Password
        :type password: str
        '''
        super(IntegrationClient, self).__init__(connection_string)
        self.__sessionId = None
        self._username = username
        self._password = password

    def is_auth(self):
        return self.__sessionId is not None
