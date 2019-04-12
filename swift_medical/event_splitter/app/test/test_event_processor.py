import unittest
from unittest.mock import MagicMock, patch
from app.test.base import BaseTestCase
from app.main.util.event_processor import StartEvent, SchemaValidationError

class TestEventProcessor(BaseTestCase):

  def test_start_event_deserialization(self):
    payload = {
      "event_type": "start",
      "message_id": "061371f1-eda5-4fea-96ee-436a6dd4f8d7",
      "message_at": "2018-09-21T18:04:55+00:00",
      "event_at": "2018-09-21T18:03:55+00:00",
      "match_id": "ef4146ee-64e3-430b-b6af-b12671e4beef",
      "location": "toronto",
      "team_1": "Toronto",
      "team_2": "Montreal"
    }
    event = StartEvent(payload)
    result = event.deserialize()
    self.assertEquals(result.errors, {})

  def test_start_event_deserialization_error(self):
    payload = {
      "event_type": "start",
      "message_id": "061371f1-eda5-4fea-96ee-436a6dd4f8d7",
    }
    event = StartEvent(payload)
    self.assertRaises(SchemaValidationError, event.deserialize)

  @patch('app.main.util.event_processor.Kafka')
  def test_publish_to_kafka(self, mock_kafka):
    payload = {
      "event_type": "start",
      "message_id": "061371f1-eda5-4fea-96ee-436a6dd4f8d7",
      "message_at": "2018-09-21T18:04:55+00:00",
      "event_at": "2018-09-21T18:03:55+00:00",
      "match_id": "ef4146ee-64e3-430b-b6af-b12671e4beef",
      "location": "toronto",
      "team_1": "Toronto",
      "team_2": "Montreal"
    }
    event = StartEvent(payload)
    event.process()
    mock_kafka.return_value.publish_event.assert_called()

if __name__ == '__main__':
  unittest.main()
