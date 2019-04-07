from ..util.event_processor import build_event_processor
from flask import current_app as app

def parse_event(data):
  app.logger.info("parse_event")
  event_processor = build_event_processor(data)
  event_processor.process()