import enum
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Match(db.Model):
  __tablename__ = "Match"
  
  match_id = db.Column(db.String(36), nullable=False, primary_key=True)
  team_1 = db.Column(db.String(300),nullable=False)
  team_2 = db.Column(db.String(300),nullable=False)
  team_1_score = db.Column(db.Integer, default=0, nullable=False)
  team_2_score = db.Column(db.Integer, default=0,nullable=False)
  match_date = db.Column(db.DateTime, nullable=True)

  def as_json(self):
    return {
      'match_id': self.match_id,
      'team_1': {
        'name': self.team_1,
        'score': self.team_1_score
      },
      'team_2': {
        'name': self.team_2,
        'score': self.team_2_score
      },
      'match_date': str(self.match_date)
    }
