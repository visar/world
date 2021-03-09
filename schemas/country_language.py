from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import validate


class CountryLanguageSchema(Schema):
    class Meta:
        ordered = True

    language = fields.String(required=True)
    isofficial = fields.Boolean(required=True)
    percentage = fields.Float(required=True)
