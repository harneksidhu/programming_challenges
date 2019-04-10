from flask import request, Blueprint

from flask import current_app as app

from ..service.event_service import export_event, save_event

event_api = Blueprint('event_api', __name__, url_prefix='/')


@event_api.route('/events', methods=['GET'])
def get_event():
  app.logger.info("get_event")
  event_id = request.args.get('event_id')
  event_format = request.args.get('Format')
  app.logger.info(event_id)
  app.logger.info(event_format)
  return export_event(event_id, event_format)

@event_api.route('/events', methods=['POST'])
def post_event():
    app.logger.info("post_event")
    app.logger.info(request.data)
    data = request.json
    app.logger.info(data)
    payload = data['payload']
    payload['event_type'] = data['topic']
    return save_event(payload)
