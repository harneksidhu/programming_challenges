from confluent_kafka import Consumer, TopicPartition, KafkaError
import requests
import json

c = Consumer({
  'bootstrap.servers': 'kafka:9092',
  'group.id': 'score_consumer',
  'auto.offset.reset': 'smallest',
  'enable.auto.commit': 'false'
})

c.subscribe(['start','goal'])

def submit_request_to_event_api(payload, topic):
  r = requests.post('http://score-api:5000/{}'.format(topic), json=payload)
  print(r.json())
  r.raise_for_status()

while True:
  msg = c.poll(1.0)
  if msg is None:
    continue
  if msg.error():
    print("Consumer error: {}".format(msg.error()))
    break
  payload = json.loads(msg.value().decode('ascii'))
  print('Received message: {} Topic: {} Offset: {}'.format(payload, msg.topic(), msg.offset()))
  submit_request_to_event_api(payload[0], msg.topic())
  c.commit(msg)
c.close()
