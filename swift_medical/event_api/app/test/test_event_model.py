import unittest
import datetime
import yaml
from app.main.model.event import FifaEvent
from app.test.base import BaseTestCase
from app.main import db

class TestExportEvent(BaseTestCase):

  def test_json(self):
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
    self.assertEquals(event.as_json(), 
      {
      "event_type": "start",
      "message_id": "061371f1-eda5-4fea-96ee-436a6dd4f8d7",
      "message_at": "2019-04-11 23:16:48.247113",
      "event_at": "2019-04-11 23:16:48.247113",
      "match_id": "ef4146ee-64e3-430b-b6af-b12671e4beef",
      "location": "toronto",
      "team_1": "toronto",
      "team_2": "montreal",
      "player_first_name": "None",
      "player_id": "None",
      "player_last_name": "None",
      "player_team": "None"
      }
    )

  def test_yaml(self):
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

    #TODO: Figure out a way to construst a raw yaml payload
    self.assertEquals(event.as_yaml(), yaml.dump(event.as_json()))

if __name__ == '__main__':
  unittest.main()
