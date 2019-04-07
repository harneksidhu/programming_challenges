from flask import request, Blueprint

from flask import current_app as app

from ..service.event_service import parse_event

event_splitter = Blueprint('event_splitter', __name__, url_prefix='/')

@event_splitter.route('/events', methods=['POST'])
def split_event():
    app.logger.info("split event!!")
    data = request.json
    app.logger.info(data)
    return parse_event(data)
