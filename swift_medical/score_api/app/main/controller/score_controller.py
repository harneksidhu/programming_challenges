from flask import request, Blueprint

from flask import current_app as app

from ..service.score_service import get_score_data, save_start_event

score_api = Blueprint('score_api', __name__, url_prefix='/')


@score_api.route('/score', methods=['GET'])
def get_score():
  app.logger.info("get_score")
  return get_score_data(request.args.to_dict())

@score_api.route('/start', methods=['POST'])
def post_start_event():
    app.logger.info("post_start_event")
    data = request.json
    return save_start_event(data)
