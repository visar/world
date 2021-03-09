from http import HTTPStatus

from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from models.city import City
from models.country import Country
from models.country_language import CountryLanguage
from schemas.country import CountrySchema
from utils import gen_id

country_schema = CountrySchema()
country_list_schema = CountrySchema(many=True)


class CountryListResource(Resource):
    def get(self):
        countries = Country.get_all()

        return country_list_schema.dump(countries), HTTPStatus.OK


class CountryResource(Resource):
    def get(self, country_code):
        country = Country.get_by_countrycode(country_code=country_code)

        if country is None:
            return {'message': 'Country not found.'}, HTTPStatus.NOT_FOUND

        country.cities = City.get_by_countrycode(country_code)
        country.languages = CountryLanguage.get_by_countrycode(country_code)

        return country_schema.dump(country), HTTPStatus.OK
