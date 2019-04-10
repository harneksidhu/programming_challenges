from flask import make_response, jsonify
from ..model.event import db, FifaEvent
from sqlalchemy import exc
from ..util.utilities import convert_to_datetime
from flask import current_app as app
import traceback

def export_event(event_id, event_format):
  try:
    event = FifaEvent.query.filter_by(message_id=event_id).first()
    if event:
      if event_format == 'json':
        response = event.as_json()
        return make_response(jsonify(response), 200)
      elif event_format == 'yaml':
        response = event.as_yaml()
        return make_response(response, 200)
      else:
        return make_response(jsonify(error='bad request'), 400)
    else: 
      return make_response(jsonify(error='event not found'), 404)
  except Exception as e:
    app.logger.error(traceback.print_exc())
    return make_response(jsonify(error=e.args), 500)

def save_event(data):
  try:
    event = FifaEvent.query.filter_by(message_id=data['message_id']).first()
    if not event:
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
