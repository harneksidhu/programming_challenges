from kafka import KafkaConsumer
import json
import requests

def store_event_to_event_db(payload):
  r = requests.post('http://event-api:5000/events', data=payload)
  r.raise_for_status()

topics = ['start','goal', 'pass', 'save', 'end']
consumer = KafkaConsumer(bootstrap_servers=['kafka:9092'], group_id='event_consumer', enable_auto_commit=False, value_deserializer=lambda m: json.loads(m.decode('ascii')))
consumer.subscribe(topics)
print("Starting Consumer")
while True:
  for msg in consumer:
    print("Message received")
    print(msg)
    store_event_to_event_db(msg.value[0])
    print("commit offset")
    consumer.commit()
    print("offset comitted")
consumer.close(autocommit=False)
