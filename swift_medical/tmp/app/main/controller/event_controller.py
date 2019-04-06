from flask import request
from flask_restplus import Resource

from ..service.event_service import parse_event

from ..util.dto import EventDto

api = EventDto.api

@api.route('/')
class Event(Resource):
  def post(self):
    """Creates a new Event """
    data = request.json
    return parse_event(data)
