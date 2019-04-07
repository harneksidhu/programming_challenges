from ..util.event_processor import build_event_processor, SchemaValidationError
from flask import make_response, jsonify

def parse_event(data):
  try:
    event_processor = build_event_processor(data)
    event_processor.process()
    return make_response(jsonify(), 200)
  except SchemaValidationError as e:
    return make_response(jsonify(error=e.args), 400)
  # except Exception as e:
  #   return make_response(jsonify(error="Internal system error"), 500)
