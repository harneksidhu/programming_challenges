import abc
from .event_schema import MatchActionSchema, PlayerActionSchema
from .kafka import Kafka

class SchemaValidationError(Exception):
  def __init__(self, arg):
    self.args = arg


class EventProcessor:
  def __init__(self, data):
    self.data = data
    self.schema = self.schema()()

  @abc.abstractmethod
  def schema(self):
    pass

  @abc.abstractmethod
  def topic(self):
    pass

  def deserialize(self):
    result = self.schema.load(self.data)
    if len(result.errors)>0:
      raise SchemaValidationError(result.errors)
    return result

  def publish_to_kafka(self, deserialized_object):
    payload = self.schema.dump(deserialized_object.data)
    Kafka().publish_event(self.topic(), payload)

  def process(self):
    deserialized_object = self.deserialize()
    self.publish_to_kafka(deserialized_object)

class StartEvent(EventProcessor):
  def schema(self):
    return MatchActionSchema

  def topic(self):
    return 'start'

class GoalEvent(EventProcessor):
  def schema(self):
    return PlayerActionSchema

  def topic(self):
    return 'goal'

class PassEvent(EventProcessor):
  def schema(self):
    return PlayerActionSchema

  def topic(self):
    return 'pass'

class SaveEvent(EventProcessor):
  def schema(self):
    return PlayerActionSchema

  def topic(self):
    return 'save'

class EndEvent(EventProcessor):
  def schema(self):
    return MatchActionSchema

  def topic(self):
    return 'end'

event_processor_by_type = {
  'start': StartEvent,
  'goal': GoalEvent,
  'pass': PassEvent,
  'save': SaveEvent,
  'end': EndEvent
}

def build_event_processor(data):
  print('build_event_processor')
  print(data)
  event_processor = event_processor_by_type[data['event_type']]
  return event_processor(data)
