from context import selection
from selection.integration import IntegrationClient
from selection.proto import CountryMessages_pb2, DocumentMessages_pb2, LaunchContentMessages_pb2, LaunchHistoryElementMessages_pb2, SpacecraftTypeMessages
import unittest

#todo : add more tests
class IntegrationTest(unittest.TestCase):

    proto_list = {
        "ru.nicetu.integration.messages.CountryMessages$CountryGetRequest": CountryMessages_pb2.CountryGetRequest,
        "ru.nicetu.integration.messages.SpacecraftTypeMessages$SpacecraftTypeGetRequest": SpacecraftTypeMessages.SpacecraftTypeGetRequest,
        "ru.nicetu.integration.messages.DocumentMessages$DocumentGetResponse": DocumentMessages_pb2.DocumentGetResponse,
        "ru.nicetu.integration.messages.LaunchContentMessages$LaunchContentGetResponse": LaunchContentMessages_pb2.LaunchContentGetResponse,
        "ru.nicetu.integration.messages.LaunchHistoryElementMessages$LaunchHistoryElementStoreRequest": LaunchHistoryElementMessages_pb2.LaunchHistoryElementStoreRequest
    }

    # probably useless
    def test_get_java_class(self):
        for k, v in self.proto_list.items():
            self.assertEqual(IntegrationClient.get_java_class(v), k)




if __name__ == '__main__':
    unittest.main()