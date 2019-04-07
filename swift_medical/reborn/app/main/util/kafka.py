#!/usr/bin/env python
from kafka import KafkaProducer
import json

class Kafka():
  def __init__(self):
    self.producer = KafkaProducer(bootstrap_servers=['kafka:9092'], 
                                  retries=5,
                                  value_serializer=lambda m: json.dumps(m).encode('ascii'))

  def publish_event(self, topic, payload):
    self.producer.send(topic, payload)
    # block until all async messages are sent
    self.producer.flush()
    # tidy up the producer connection
    self.producer.close()
