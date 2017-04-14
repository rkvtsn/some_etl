#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import time
import os

from controller import Controller
from radient import RadientClient


class RadientController(Controller):

    def load(self):
        pass

    @property
    def service_name(self):
        return "radient"

    def __init__(self, selection_engine=None, client=None, xml_encoding=None):
        super(RadientController, self).__init__(selection_engine=selection_engine, client=client)
        if xml_encoding is None:
            xml_encoding = 'cp1251' # it's for Windows OS
        self.xml_encoding = xml_encoding
        self.__xml_requests = {}

    def _load_req_body(self, name, t=None):
        if t is None:
            t = time.time()
        if self.__xml_requests.has_key(name):
            x = self.__xml_requests[name]
        else:
            directory = os.path.dirname(os.path.abspath(__file__))
            with open('%s\\%s.xml' % (directory, name), 'r') as file_xml:
                x = file_xml.read()
        return x.replace('%time', str(int(t)))

    def extract_mapping_settings(self):
        settings = {
            "uch": {
                "body": self._load_req_body('uch'),
                "encoding": self.xml_encoding
            },
            "spacecraft": {
                "body": self._load_req_body('spacecraft'),
                "encoding": self.xml_encoding
            },
            "ziprem": {
                "body": self._load_req_body('ziprem'),
                "encoding": self.xml_encoding
            },
        }
        return settings

    def _default_client(self):
        # todo move to settings file
        config = { "connection_string": "http://192.168.50.51:3005/jboss/servlet/POESOServlet",
                   "encoding": "KOI8" }
        return RadientClient(**config)


if __name__ == "__main__":
    with RadientController() as controller:
        source = controller.extract()
        target = controller.transform(source)
        print target['rpsn_main'].head()


"""
: {
    "expression": {
      "1": "to_number(x.uchgroupname)"
    }
  }
"""
