from flask_restplus import Namespace, fields

class EventDto:
  api = Namespace('Event', description='Fifa world cup related events')
