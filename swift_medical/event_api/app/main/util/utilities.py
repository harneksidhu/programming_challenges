from datetime import datetime
import pytz

def convert_to_datetime(date_string, timezone=pytz.UTC):
  datetime_object = datetime.strptime(date_string,'%Y-%m-%dT%H:%M:%S+00:00')
  datetime_object = datetime_object.replace(tzinfo=timezone)
  return datetime_object
