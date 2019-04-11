from marshmallow import fields, Schema, validates, ValidationError

class GetEventSchema(Schema):
  event_id = fields.Str(required=True)
  Format = fields.Str(required=True)

  @validates('Format')
  def validate_format(self, val):
    if val not in ['yaml', 'json']:
        raise ValidationError('Format must be either yaml or json')

class SaveEventSchema(Schema):
  message_id = fields.Str(required=True)
  match_id = fields.Str(required=True)
  message_at = fields.DateTime(required=True)
  event_at = fields.DateTime(required=True)
  event_type = fields.Str(required=True)
  location = fields.Str(required=False)
  team_1 = fields.Str(required=False)
  team_2 = fields.Str(required=False)
  player_id = fields.Str(required=False)
  player_first_name = fields.Str(required=False)
  player_last_name = fields.Str(required=False)
  player_team = fields.Str(required=False)
