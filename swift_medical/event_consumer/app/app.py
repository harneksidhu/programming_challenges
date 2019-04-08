from confluent_kafka import Consumer, TopicPartition, KafkaError
import requests
import json

c = Consumer({
  'bootstrap.servers': 'kafka:9092',
  'group.id': 'event_consumer',
  'auto.offset.reset': 'smallest',
  'enable.auto.commit': 'false'
})

c.subscribe(['start','goal', 'pass', 'save', 'end'])

while True:
  msg = c.poll(1.0)
  if msg is None:
    continue
  if msg.error():
    print("Consumer error: {}".format(msg.error()))
    break
  payload = json.loads(msg.value().decode('ascii'))
  print('Received message: {} Topic: {} Offset: {}'.format(payload, msg.topic(), msg.offset()))
  r = requests.post('http://event-api:5000/events', json={'payload': payload[0], 'topic': msg.topic()})
  r.raise_for_status()
  c.commit(msg)

c.close()
