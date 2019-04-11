from flask import make_response, jsonify
from ..model.score import db, Match
from sqlalchemy import exc
from flask import current_app as app
import traceback
from ..util.score_schema import GetScoreSchema, SaveGoalSchema, SaveStartSchema

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
      # Handle case where goal event comes first before start event
      if match.team_1 is deserialized_payload.data['team_2']:
        match.team_2_score = match.team_1_score
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
  deserialized_payload = SaveGoalSchema().load(data)
  if len(deserialized_payload.errors)>0:
    app.logger.info(deserialized_payload.errors)
    return make_response(jsonify(error='bad request'), 400)
  try:
    match = Match.query.filter_by(match_id=deserialized_payload.data['match_id']).first()
    if not match:
      match = Match({ 
        'match_id': deserialized_payload.data['match_id'],
        'team_1': deserialized_payload.data['player_team'],
        'team_1_score': 1
      })
      save_changes(match)
      return make_response(jsonify(), 200)
    else:
      if match.team_1 is deserialized_payload.data['player_team']:
        match.team_1_score += match.team_1_score
      else:
        match.team_2_score += match.team_2_score
      save_changes(match)
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
