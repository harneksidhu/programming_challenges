from flask import make_response, jsonify
from ..model.event import db, FifaEvent
from sqlalchemy import exc
from flask import current_app as app
import traceback
from ..util.event_schema import GetEventSchema, SaveEventSchema

def export_event(payload):
  deserialized_payload = GetEventSchema().load(payload)
  if len(deserialized_payload.errors)>0:
    return make_response(jsonify(error='bad request'), 400)
  try:
    data = deserialized_payload.data
    event = FifaEvent.query.filter_by(message_id=data['event_id']).first()
    if not event:
      return make_response(jsonify(error='event not found'), 404)
    else:
      if data['Format'] == 'json':
        response = event.as_json()
        return make_response(jsonify(response), 200)
      elif data['Format'] == 'yaml':
        response = event.as_yaml()
        return make_response(response, 200)
  except Exception as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 500)

def save_event(payload):
  deserialized_payload = SaveEventSchema().load(payload)
  if len(deserialized_payload.errors)>0:
    return make_response(jsonify(error='bad request'), 400)
  try:
    data = deserialized_payload.data
    event = FifaEvent.query.filter_by(message_id=data['message_id']).first()
    if not event:
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
