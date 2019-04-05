import abc
from .event_schema import MatchActionSchema, PlayerActionSchema

class EventProcessor:
  
  def __init__(self, data):
    self.data = data

  @abc.abstractmethod
  def schema(self):
    pass

  @abc.abstractmethod
  def topic(self):
    pass

  @abc.abstractmethod
  def deserialize(self):
    schema = self.schema()
    result = schema.load(self.data)
    return result

  def publish_to_kafka(self, deserialized_object):


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

event_by_name = {
  'start': StartEvent,
  'goal': GoalEvent,
  'pass': PassEvent,
  'save': SaveEvent,
  'end': EndEvent
}