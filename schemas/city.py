from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import validate


class CitySchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    countrycode = fields.String(required=True,
                                validate=[validate.Length(max=3)])
    district = fields.String(required=True)
    population = fields.Integer(required=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
