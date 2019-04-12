import unittest
from unittest.mock import MagicMock, patch
from app.test.base import BaseTestCase
from app.main.util.kafka import Kafka

class TestKafka(BaseTestCase):

  @patch('app.main.util.kafka.KafkaProducer')
  def test_event_publish(self, mock_kafka_producer):
    topic = 'start'
    payload = {}
    Kafka().publish_event(topic, payload)
    mock_kafka_producer.return_value.send.assrt_called_once_with(topic, payload)

if __name__ == '__main__':
  unittest.main()
