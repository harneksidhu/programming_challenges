from flask import request, Blueprint

from ..service.event_service import parse_event

event_splitter = Blueprint('event_splitter', __name__, url_prefix='/')

@event_splitter.route('/')
def hello():
    return "Hello World!"
