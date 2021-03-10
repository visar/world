from http import HTTPStatus

from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_kwargs

from models.city import City
from models.country import Country
from models.country_language import CountryLanguage
from schemas.country import CountrySchema

country_schema = CountrySchema()
country_list_schema = CountrySchema(many=True)


class CountryListResource(Resource):
    @use_kwargs({'region': fields.String(missing=None)}, location='query')
    def get(self, region):
        countries = Country.get_all_by_region(region=region)

        if countries is None:
            return {'message': 'Could not find any country.'}, HTTPStatus.NOT_FOUND

        return country_list_schema.dump(countries), HTTPStatus.OK


class CountryResource(Resource):
    def get(self, country_code):
        country = Country.get_by_countrycode(country_code=country_code)

        if country is None:
            return {'message': 'Country not found.'}, HTTPStatus.NOT_FOUND

        country.cities = City.get_by_countrycode(country_code)
        country.languages = CountryLanguage.get_by_countrycode(country_code)

        return country_schema.dump(country), HTTPStatus.OK
