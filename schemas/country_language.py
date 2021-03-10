from marshmallow import Schema
from marshmallow import fields


class CountryLanguageSchema(Schema):
    class Meta:
        ordered = True

    language = fields.String(required=True)
    isofficial = fields.Boolean(required=True)
    percentage = fields.Float(required=True)
