#!/usr/bin/env python
from kafka import KafkaConsumer

consumer = KafkaConsumer('messages', group_id='event_consumer')

while True:
  for msg in consumer:
    print (msg)
consumer.close()