import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StateEnum(enum.Enum):
  SAVED = 'SAVED'
  STARTED = 'STARTED'
  ENDED = 'ENDED'

class FifaEvent(db.Model):
  __tablename__ = "FifaEvent"

  message_id = db.Column(db.String(36), primary_key=True)
  match_id = db.Column(db.String(36), nullable=False)
  message_at = db.Column(db.DateTime, nullable=False)
  event_at = db.Column(db.DateTime, nullable=False)
  event_type = db.Column(db.Enum(StateEnum), nullable=False)
  __mapper_args__ = {'polymorphic_on': event_type}

class MatchAction(FifaEvent):
  __mapper_args__ = {'polymorphic_identity': 'match_action'}
  location = db.Column(db.String(300), nullable=False)
  team1 = db.Column(db.String(300), nullable=False)
  team2 = db.Column(db.String(300), nullable=False)

class PlayerAction(FifaEvent):
  __mapper_args__ = {'polymorphic_identity': 'player_action'}
  player_id = db.Column(db.String(36), nullable=False)
  player_first_name = db.Column(db.String(100), nullable=False)
  player_last_name = db.Column(db.String(100), nullable=False)
  player_team = db.Column(db.String(300), nullable=False)
