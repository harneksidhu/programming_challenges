import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StateEnum(enum.Enum):
  START = 'start'
  GOAL = 'goal'
  PASS = 'pass'
  SAVE = 'save'
  END = 'end'

class FifaEvent(db.Model):
  __tablename__ = "FifaEvent"

  message_id = db.Column(db.String(36), primary_key=True)
  match_id = db.Column(db.String(36), nullable=False)
  message_at = db.Column(db.DateTime, nullable=False)
  event_at = db.Column(db.DateTime, nullable=False)
  event_type = db.Column(db.Enum('start','goal','pass','save','end'), nullable=False)
  location = db.Column(db.String(300))
  team_1 = db.Column(db.String(300))
  team_2 = db.Column(db.String(300))
  player_id = db.Column(db.String(36))
  player_first_name = db.Column(db.String(100))
  player_last_name = db.Column(db.String(100))
  player_team = db.Column(db.String(300))
