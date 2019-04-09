from flask import make_response, jsonify
from ..model.event import db, FifaEvent
from sqlalchemy import exc
from datetime import datetime

def save_event(data):
  try:
    event = FifaEvent.query.filter_by(message_id=data['message_id']).first()
    if not event:
      data['message_at'] = datetime.strptime(data['message_at'],'%Y-%m-%dT%H:%M:%S+00:00')
      data['event_at'] = datetime.strptime(data['event_at'],'%Y-%m-%dT%H:%M:%S+00:00')
      new_event = FifaEvent(**data)
      save_changes(new_event)
    return make_response(jsonify(), 200)
  except exc.SQLAlchemyError as e:
    return make_response(jsonify(error=e.args), 400)
  except Exception as e:
    return make_response(jsonify(error=e.args), 500)

def save_changes(data):
  db.session.add(data)
  db.session.commit()
