from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import validate

from schemas.city import CitySchema
from schemas.country_language import CountryLanguageSchema


class CountrySchema(Schema):
    class Meta:
        ordered = True

    code = fields.String(required=True,
                         validate=[validate.Length(max=3)])
    name = fields.String(required=True)
    continent = fields.String(required=True,
                              validate=lambda c: c in ['Asia',
                                                       'Europe',
                                                       'North America',
                                                       'Africa',
                                                       'Oceania',
                                                       'Antarctica',
                                                       'South America'])

    region = fields.String(required=True)
    surfacearea = fields.Float(required=True)
    indepyear = fields.Integer()
    population = fields.Integer(required=True)
    lifeexpectancy = fields.Float()
    gnp = fields.Number()
    gnpold = fields.Number()
    localname = fields.String(required=True)
    governmentform = fields.String(required=True)
    headofstate = fields.String()
    code2 = fields.String(required=True,
                          validate=[validate.Length(max=2)])
    capital = fields.Nested(CitySchema,
                            attribute='city',
                            # only=('id',)
                            )
    cities = fields.List(fields.Nested(CitySchema))
    languages = fields.List(fields.Nested(CountryLanguageSchema))

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
