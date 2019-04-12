import unittest
from unittest.mock import MagicMock, patch
from app.main.service.event_service import parse_event
from app.main.util.event_processor import build_event_processor, SchemaValidationError
from app.test.base import BaseTestCase

class TestParseEvent(BaseTestCase):

  @patch('app.main.service.event_service.build_event_processor')
  def test_200_response(self, mock_build_event_processor):
    mock_build_event_processor.return_value = MagicMock()
    response = parse_event({})
    self.assertEquals(response._status_code, 200)

  @patch('app.main.service.event_service.build_event_processor')
  def test_400_response(self, mock_build_event_processor):
    mock_build_event_processor.side_effect = SchemaValidationError('error')
    response = parse_event({})
    self.assertEquals(response._status_code, 400)

  @patch('app.main.service.event_service.build_event_processor')
  def test_500_response(self, mock_build_event_processor):
    mock_build_event_processor.side_effect = Exception('error')
    response = parse_event({})
    self.assertEquals(response._status_code, 500)

if __name__ == '__main__':
  unittest.main()
