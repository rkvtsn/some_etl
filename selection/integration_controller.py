#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from controller import Controller
from integration import IntegrationClient

import proto
import proto_manager as pm


class IntegrationController(Controller):
    def load(self):
        pass

    @property
    def service_name(self):
        return "integration"

    def __init__(self, selection_engine=None, client=None):
        super(IntegrationController, self).__init__(selection_engine=selection_engine, client=client)

    def extract_mapping_settings(self):
        settings = {
            "spacecrafttype": {
                "body": pm.proto_select_all(proto.SpacecraftTypeMessages.SpacecraftTypeGetRequest),
                "java_class": "ru.nicetu.integration.messages.SpacecraftTypeMessages$SpacecraftTypeGetRequest",
                "proto_response": proto.SpacecraftTypeMessages.SpacecraftTypeGetResponse
            },
            "devicetype": {
                "body": pm.proto_select_all(proto.DeviceTypeMessages.DeviceTypeGetRequest),
                "java_class": "ru.nicetu.integration.messages.DeviceTypeMessages$DeviceTypeGetRequest",
                "proto_response": proto.DeviceTypeMessages.DeviceTypeGetResponse
            },
        }
        return settings

    def _default_client(self):
        # todo move to settings file
        config = {"connection_string": "tcp://localhost:61613",
                  "username": "selection",
                  "password": "12345678"}
        return IntegrationClient(**config)


if __name__ == "__main__":
    with IntegrationController() as controller:
        source = controller.extract()
        target = controller.transform(source)
        print target['rpsn_main'].head()