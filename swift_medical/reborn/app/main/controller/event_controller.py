from flask import request, Blueprint

from ..service.event_service import parse_event

event_splitter = Blueprint('event_splitter', __name__, url_prefix='/')

@event_splitter.route('/events', methods=['POST'])
def split_event():
    data = request.json
    return parse_event(data)
