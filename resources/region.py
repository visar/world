from http import HTTPStatus

from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_kwargs

from models.country import Country
from schemas.region import RegionSchema

region_list_schema = RegionSchema(many=True)


class RegionListResource(Resource):
    @use_kwargs({'continent': fields.String(missing=None)}, location='query')
    def get(self, continent):
        regions = Country.get_all_regions_of_continent(continent=continent)

        if regions is None:
            return {'message': 'Could not find any region.'}, HTTPStatus.NOT_FOUND

        return region_list_schema.dump([{"name": region[0]} for region in regions]), HTTPStatus.OK
