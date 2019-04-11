from flask import make_response, jsonify
from ..model.score import db, Match
from sqlalchemy import exc
from flask import current_app as app
import traceback
from ..util.score_schema import GetScoreSchema, SaveGoalSchema, SaveStartSchema

def create_default_match_object(payload):
  match = Match(**payload)

def get_score_data(data):
  app.logger.info(data)
  deserialized_payload = GetScoreSchema().load(data)
  if len(deserialized_payload.errors)>0:
    return make_response(jsonify(error='bad request'), 400)
  match = Match.query.filter_by(match_id=deserialized_payload.data['match_id']).first()
  if not match:
    return make_response(jsonify(error='match not found'), 404)
  else:
    return make_response(jsonify(match.as_json()), 200)

def save_start_event(data):
  deserialized_payload = SaveStartSchema().load(data)
  if len(deserialized_payload.errors)>0:
    app.logger.info(deserialized_payload.errors)
    return make_response(jsonify(error='bad request'), 400)
  try:
    match = Match.query.filter_by(match_id=deserialized_payload.data['match_id']).first()
    if not match:
      match = Match(**deserialized_payload.data)
      save_changes(match)
      return make_response(jsonify(), 200)
    else:
      match.update(**deserialized_payload.data)
      save_changes(match)
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

def save_changes(data):
  db.session.add(data)
  db.session.commit()
