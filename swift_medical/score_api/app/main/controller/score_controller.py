from flask import request, Blueprint

from flask import current_app as app

from ..service.score_service import get_score_data

score_api = Blueprint('score_api', __name__, url_prefix='/')


@score_api.route('/score', methods=['GET'])
def get_score():
  app.logger.info("get_score")
  return get_score_data(request.args.to_dict())

@score_api.route('/events', methods=['POST'])
def post_event():
    app.logger.info("post_event")
    app.logger.info(request.data)
    data = request.json
    app.logger.info(data)
    payload = data['payload']
    payload['event_type'] = data['topic']
    return save_event(payload)
