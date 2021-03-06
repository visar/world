from http import HTTPStatus

from flask_restful import Resource

from ..extensions import cache
from ..models.country import Country
from ..schemas.continent import ContinentSchema

continent_list_schema = ContinentSchema(many=True)


class ContinentListResource(Resource):
    @cache.cached(timeout=60, query_string=True)
    def get(self):
        continents = Country.get_continents()

        if continents is None:
            return {'message': 'Could not find any continent.'}, HTTPStatus.NOT_FOUND

        return continent_list_schema.dump([{"name": continent[0]} for continent in continents]), HTTPStatus.OK
