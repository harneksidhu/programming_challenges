from marshmallow import Schema, fields

class GetScoreSchema(Schema):
  match_id = fields.Str(required=True)

class SaveGoalSchema(Schema):
  match_id = fields.Str(required=True)
  player_team = fields.Str(required=True)

class SaveStartSchema(Schema):
  match_id = fields.Str(required=True)
  team_1 = fields.Str(required=True)
  team_2 = fields.Str(required=True)
  match_date = fields.DateTime(required=True, load_from="event_at")
