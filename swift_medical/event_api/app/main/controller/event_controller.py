from flask import request, Blueprint
from flask import current_app as app
from ..service.event_service import export_event, save_event

event_api = Blueprint('event_api', __name__, url_prefix='/')

@event_api.route('/events', methods=['GET'])
def get_event():
  app.logger.info("get_event")
  return export_event(request.args.to_dict())

@event_api.route('/events', methods=['POST'])
def post_event():
    app.logger.info("post_event")
    data = request.json
    payload = data['payload']
    payload['event_type'] = data['topic']
    return save_event(payload)
