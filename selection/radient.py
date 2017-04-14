#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import urllib2

import requests

from client import Client


class RadientClient(Client):
    """Radient http-client. Send/receive xml requests."""

    def disconnect(self):
        pass

    def connect(self):
        pass

    empty_response = "<response />"

    default_headers = {'Content-Type': 'application/xml'}

    def __add_xml_header(self, body):
        xml = '<?xml version="1.0" encoding="%s"?>' % self._encoding
        xml += body
        return xml

    def __init__(self, connection_string, encoding):
        super(RadientClient, self).__init__(connection_string)
        self._encoding = encoding

    def check_connection(self):
        try:
            urllib2.urlopen(self.connection_string, timeout=1)
            return True
        except urllib2.URLError as err:
            print "[connection failed]: %s" % err
            return False

    def request(self, data, **kwargs):
        headers = kwargs.get('headers', self.default_headers)
        req = requests.post(self.connection_string,
                            data=self.__add_xml_header(data),
                            headers=headers)

        # todo: check encoding in Astro Linux
        response = req.text.encode(req.encoding) # 'latin-1'

        return response, req.status_code
