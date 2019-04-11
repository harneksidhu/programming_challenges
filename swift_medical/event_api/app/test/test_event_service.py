import unittest
import datetime
from app.main.service.event_service import export_event, save_event
from app.main.model.event import FifaEvent
from app.test.base import BaseTestCase
from app.main import db

class TestExportEvent(BaseTestCase):

  def test_missing_format(self):
    payload = {
      'event_id': '061371f1'
    }
    response = export_event(payload)
    self.assertEquals(response.json, dict(error='bad request'))
    self.assertEquals(response._status_code, 400)

  def test_missing_event(self):
    payload = {
      'Format': 'yaml'
    }
    response = export_event(payload)
    self.assertEquals(response.json, dict(error='bad request'))
    self.assertEquals(response._status_code, 400)

  def test_incorrect_format(self):
    payload = {
      'event_id': '061371f1',
      'Format': 'incorrect'
    }
    response = export_event(payload)
    self.assertEquals(response.json, dict(error='bad request'))
    self.assertEquals(response._status_code, 400)

  def test_event_not_found(self):
    payload = {
      'event_id': '061371f1',
      'Format': 'yaml'
    }
    response = export_event(payload)
    self.assertEquals(response.json, dict(error='event not found'))
    self.assertEquals(response._status_code, 404)

  def test_event_found(self):
    payload = {
      'event_id': '061371f1-eda5-4fea-96ee-436a6dd4f8d7',
      'Format': 'yaml'
    }
    event = FifaEvent(
      message_id='061371f1-eda5-4fea-96ee-436a6dd4f8d7',
      match_id='ef4146ee-64e3-430b-b6af-b12671e4beef',
      message_at=datetime.datetime(2019, 4, 11, 23, 16, 48, 247113),
      event_at=datetime.datetime(2019, 4, 11, 23, 16, 48, 247113),
      event_type='start',
      location='toronto',
      team_1='toronto',
      team_2='montreal'
    )
    db.session.add(event)
    db.session.commit()
    response = export_event(payload)
    self.assertEquals(response._status_code, 200)

class TestSaveEvent(BaseTestCase):

  def test_bad_payload(self):
    payload = {
      "event_type": "start",
      "message_at": "2018-09-21T18:04:55+00:00",
      "event_at": "2018-09-21T18:03:55+00:00",
      "match_id": "ef4146ee-64e3-430b-b6af-b12671e4beef",
      "location": "toronto"
    }
    response = save_event(payload)
    self.assertEquals(response.json, dict(error='bad request'))
    self.assertEquals(response._status_code, 400)

  def test_correct_payload(self):
    payload = {
      "event_type": "start",
      "message_id": "061371f1-eda5-4fea-96ee-436a6dd4f8d7",
      "message_at": "2018-09-21T18:04:55+00:00",
      "event_at": "2018-09-21T18:03:55+00:00",
      "match_id": "ef4146ee-64e3-430b-b6af-b12671e4beef",
      "location": "toronto",
      "team_1": "Toronto",
      "team_2": "Montreal"
    }
    response = save_event(payload)
    event = FifaEvent.query.filter_by(message_id=payload['message_id']).first()
    self.assertEquals(response._status_code, 200)
    self.assertTrue(event)

if __name__ == '__main__':
  unittest.main()
