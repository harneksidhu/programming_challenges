from flask import make_response, jsonify
from ..model.event import db, MatchAction, PlayerAction, FifaEvent

event_model_by_type = {
  'start': MatchAction,
  'goal': PlayerAction,
  'pass': PlayerAction,
  'save': PlayerAction,
  'end': MatchAction
}

def save_event(data):
  try:
    event = FifaEvent.query.filter_by(message_id=data['message_id']).first()
    if not event:
      event_model = event_model_by_type[data['event_type']]
      new_event = event_model(data)
      save_changes(new_event)
      return make_response(jsonify(), 200)
    return make_response(jsonify(), 200)
  except SQLAlchemyError as e:
    return make_response(jsonify(error=e.args), 400)
  except Exception as e:
    return make_response(jsonify(error="Internal system error"), 500)

def save_changes(data):
  db.session.add(data)
  db.session.commit()
