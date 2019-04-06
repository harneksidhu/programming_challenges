from ..util.event_processor import build_event_processor

def parse_event(data):
  event_processor = build_event_processor(data)
  event_processor.process()