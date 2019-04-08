from flask import request, Blueprint

from flask import current_app as app

from ..service.event_service import save_event

event_api = Blueprint('event_api', __name__, url_prefix='/')

@event_api.route('/events', methods=['POST'])
def events_post():
    app.logger.info("save event")
    data = request.json
    app.logger.info(data)
    payload = data['payload']
    payload['event_type'] = data['topic']
    return save_event(payload)
