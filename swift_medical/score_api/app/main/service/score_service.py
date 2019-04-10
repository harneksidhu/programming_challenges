from flask import make_response, jsonify
from ..model.score import db, Match
from sqlalchemy import exc
from flask import current_app as app
import traceback
from ..util.score_schema import GetScoreSchema


def get_score_data(data):
  app.logger.info(data)
  request_paylod = GetScoreSchema().load(data)
  if len(request_paylod.errors)>0:
    return make_response(jsonify(error='bad request'), 400)
  app.logger.info(request_paylod.data)
  match = Match.query.filter_by(match_id=request_paylod.data['match_id']).first()
  if not match:
    return make_response(jsonify(error='match not found'), 404)
  else:
    return make_response(jsonify(match.as_json()), 200)

def save_start_event(data):
  try:
    match = Match.query.filter_by(match_id=data['match_id']).first()
    if not match:
      match = Match(
          match_id = data['match_id'],
          team_1 = data['team_1'],
          team_2 = data['team_2'],
          match_date = data['event_at']
      )
      save_changes(new_event)
      return make_response(jsonify(), 200)
  except exc.SQLAlchemyError as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 400)
  except Exception as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 500)

def save_goal_event(data):
  try:
    match = Match.query.filter_by(match_id=data['match_id']).first()
    if not match:
      data['message_at'] = convert_to_datetime(data['message_at'])
      data['event_at'] = convert_to_datetime(data['event_at'])
      new_event = FifaEvent(**data)
      save_changes(new_event)
    return make_response(jsonify(), 200)
  except exc.SQLAlchemyError as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 400)
  except Exception as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 500)

def create_default_match_object(payload):
  match = Match(
      match_id = data['match_id'],
      team_1 = data['team_1'],
      team_2 = data['team_2'],
      match_date = data['event_at']
  )

def save_changes(data):
  db.session.add(data)
  db.session.commit()
