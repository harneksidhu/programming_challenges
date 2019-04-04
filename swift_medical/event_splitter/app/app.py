#!/usr/bin/env python
from kafka import KafkaProducer

class Producer():
  def __init__(self):
    print("starting")
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'], retries=5)
    producer.send('messages', b'super-duper-message')
    print("Published msg -> 'super-duper-message' on Topic -> 'messages'")
    # block until all async messages are sent
    producer.flush()
    # tidy up the producer connection
    producer.close()

Producer()
while True:
  print("hi")
