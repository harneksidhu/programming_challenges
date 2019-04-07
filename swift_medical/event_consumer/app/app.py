#!/usr/bin/env python
from kafka import KafkaConsumer

consumer = KafkaConsumer('messages', group_id='event_consumer', enable_auto_commit=False)

while True:
  for msg in consumer:
    print (msg)
consumer.close(autocommit=False)