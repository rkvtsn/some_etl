#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

def proto_select_all(proto_class):
    result = proto_class()
    result.id = -1
    return result
"""
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

    body, header = self.request(login_request, java_class="ru.nicetu.integration.messages.CommonProtos$LoginRequest")

    login_response = CommonProtos.LoginResponse()
    login_response.ParseFromString(body)

    try:
        self.__sessionId = login_response.sessionId
    except:
        print 'Error with sessionId'
        self.__sessionId = None
    finally:
        return self.is_auth()
"""