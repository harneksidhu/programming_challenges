from marshmallow import Schema, fields

class FifaEventSchema(Schema):
  message_id = fields.Str()
  message_at = fields.DateTime()
  event_at = fields.DateTime()
  match_id = fields.Str()

class MatchActionSchema(FifaEventSchema):
  location = fields.Str()
  team_1 = fields.Str()
  team_2 = fields.Str()

class PlayerActionSchema(FifaEventSchema):
  player_id = fields.Str()
  player_first_name = fields.Str()
  player_last_name = fields.Str()
  player_team = fields.Str()
