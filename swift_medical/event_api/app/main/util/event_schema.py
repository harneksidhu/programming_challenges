from marshmallow import Schema, fields

class FifaEventSchema(Schema):
  message_id = fields.Str(required=True)
  message_at = fields.DateTime(required=True)
  event_at = fields.DateTime(required=True)
  match_id = fields.Str(required=True)

class MatchActionSchema(FifaEventSchema):
  location = fields.Str(required=True)
  team_1 = fields.Str(required=True)
  team_2 = fields.Str(required=True)

class PlayerActionSchema(FifaEventSchema):
  player_id = fields.Str(required=True)
  player_first_name = fields.Str(required=True)
  player_last_name = fields.Str(required=True)
  player_team = fields.Str(required=True)
