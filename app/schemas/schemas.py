 # Validação de dados (ex.: Marshmallow)

from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    # username= fields.Str(required=True, validate=validate.Length(min=1))
    password= fields.Str(required=True, validate=validate.Length(min=1))
    email= fields.Email(required=True)
