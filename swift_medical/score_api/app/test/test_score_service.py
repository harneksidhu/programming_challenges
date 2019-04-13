import unittest
from unittest.mock import MagicMock, patch
from app.test.base import BaseTestCase
from app.main import db
from app.main.model.score import Match
from app.main.service.score_service import get_score_data, save_start_event, save_goal_event

class TestGetScoreData(BaseTestCase):

  def test_bad_request(self):
    response = get_score_data({})
    self.assertEquals(response._status_code, 400)

  def test_match_not_found(self):
    response = get_score_data({'match_id': '1'})
    self.assertEquals(response._status_code, 404)

  def test_match_found(self):
    match = Match(match_id=1)
    db.session.add(match)
    db.session.commit()
    response = get_score_data({'match_id': '1'})
    self.assertEquals(response._status_code, 200)

class TestSaveStartEvent(BaseTestCase):

  def test_bad_request(self):
    response = save_start_event({})
    self.assertEquals(response._status_code, 400)

  def test_new_match(self):
    payload = {
      'match_id': '1',
      'team_1': 'Toronto',
      'team_2': 'Montreal',
      'match_date': '2018-09-21T18:03:55+00:00'
    }
    response = save_start_event(payload)
    self.assertEquals(response._status_code, 200)

  def test_match_upsert(self):
    payload = {
      'match_id': '1',
      'team_1': 'Toronto',
      'team_2': 'Montreal',
      'match_date': '2018-09-21T18:03:55+00:00'
    }
    match = Match(match_id=1, team_1='Montreal', team_2='Toronto', team_2_score=1)
    db.session.add(match)
    db.session.commit()
    response = save_start_event(payload)
    match = Match.query.filter_by(match_id=1).first()
    self.assertEquals(match.team_1, 'Toronto')
    self.assertEquals(match.team_1_score, 1)

if __name__ == '__main__':
  unittest.main()
