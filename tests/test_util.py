from context import selection
import unittest
import json

import pandas as pd

import selection.proto
import selection.proto_manager as pm
from selection import IntegrationClient
from selection.util import conv
from selection import proto


class Conv_Test(unittest.TestCase):

    def test_any_to_df(self):
        config = {"connection_string": "tcp://localhost:61613",
                  "username": "selection",
                  "password": "12345678"}
        client = IntegrationClient(**config)
        response = client.request(pm.proto_select_all(proto.SpacecraftTypeMessages.SpacecraftTypeGetRequest),
                                          java_class="ru.nicetu.integration.messages.SpacecraftTypeMessages$SpacecraftTypeGetRequest",
                                          proto_response=proto.SpacecraftTypeMessages.SpacecraftTypeGetResponse)

        if response is None:
            print "error"
        else:
            body, status = response
            df = conv.any_to_df(body)
        #todo: do some check
        pass


    def test_to_number(self):

        strings = ["1", "2.3", "3,4", "asd", None]
        numbers = [1, 2.3, 3.4, 0, 0]
        numbers_int = [1, 2, 3, 0, 0]

        conv_numbers = [conv.str_to_number(x) for x in strings]
        self.assertListEqual(conv_numbers, numbers)

        conv_numbers_int = [conv.str_to_number(x, is_int=True) for x in strings]
        self.assertListEqual(conv_numbers_int, numbers_int)


if __name__ == "__main__":
    unittest.main()
