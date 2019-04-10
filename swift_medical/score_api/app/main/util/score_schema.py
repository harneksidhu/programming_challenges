from marshmallow import Schema, fields

class GetScoreSchema(Schema):
  match_id = fields.Str(required=True)
