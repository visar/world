from http import HTTPStatus

from flask import current_app
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from ..extensions import cache
from ..models.city import City
from ..schemas.city import CitySchema
from ..utils import clear_redis_cache
from ..utils import gen_id

city_schema = CitySchema()
city_list_schema = CitySchema(many=True)


class CityListResource(Resource):
    @cache.cached(timeout=60, query_string=True)
    def get(self):
        cities = City.get_all()

        if cities is None:
            return {'message': 'Could not find any city.'}, HTTPStatus.NOT_FOUND

        return city_list_schema.dump(cities), HTTPStatus.OK

    def post(self):
        json_data = request.get_json()

        try:
            data = city_schema.load(data=json_data)
        except ValidationError as e:
            return {'message': 'Validation errors', 'errors': e.messages}, HTTPStatus.BAD_REQUEST

        city = City(**data)

        id = gen_id()
        while City.get_by_id(id) is not None:
            id = gen_id()

        city.id = id
        city.save()

        clear_redis_cache(f'{current_app.config["CACHE_KEY_PREFIX"]}*/cities*')

        return city_schema.dump(city), HTTPStatus.CREATED


class CityResource(Resource):
    @cache.cached(timeout=60, query_string=True)
    def get(self, city_id):
        city = City.get_by_id(city_id=city_id)

        if city is None:
            return {'message': 'City not found.'}, HTTPStatus.NOT_FOUND

        return city_schema.dump(city), HTTPStatus.OK

    def patch(self, city_id):
        json_data = request.get_json()

        try:
            data = city_schema.load(data=json_data, partial=(
                'name', 'countrycode', 'district', 'population'))
        except ValidationError as e:
            return {'message': 'Validation errors', 'errors': e.messages}, HTTPStatus.BAD_REQUEST

        city = City.get_by_id(city_id=city_id)

        if city is None:
            return {'message': 'City not found'}, HTTPStatus.NOT_FOUND

        city.name = data.get('name') or city.name
        city.countrycode = data.get('countrycode') or city.countrycode
        city.district = data.get('district') or city.district
        city.population = data.get('population') or city.population

        city.save()

        clear_redis_cache(f'{current_app.config["CACHE_KEY_PREFIX"]}*/cities*')

        return city_schema.dump(city), HTTPStatus.OK

    def delete(self, city_id):
        city = City.get_by_id(city_id=city_id)

        if city is None:
            return {'message': 'City not found'}, HTTPStatus.NOT_FOUND

        city.delete()

        clear_redis_cache(f'{current_app.config["CACHE_KEY_PREFIX"]}*/cities*')

        return {}, HTTPStatus.NO_CONTENT
