__title__ = 'app'
__version__ = '0.0.1'


from flask import Flask
from flask_restful import Api

from .config import Config
from .extensions import cache
from .extensions import db
from .resources.city import CityListResource
from .resources.city import CityResource
from .resources.continent import ContinentListResource
from .resources.country import CountryListResource
from .resources.country import CountryResource
from .resources.region import RegionListResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    cache.init_app(app)

    # @app.before_request
    # def before_request():
    #     print('\n==================== BEFORE REQUEST ====================\n')
    #     print(cache.cache._cache.keys())
    #     print('\n=======================================================\n')

    # @app.after_request
    # def after_request(response):
    #     print('\n==================== AFTER REQUEST ====================\n')
    #     print(cache.cache._cache.keys())
    #     print('\n=======================================================\n')
    #     return response


def register_resources(app):
    api = Api(app)

    api.add_resource(CityListResource, '/cities')
    api.add_resource(CityResource, '/cities/<int:city_id>')

    api.add_resource(CountryListResource, '/countries')
    api.add_resource(CountryResource, '/countries/<string:country_code>')

    api.add_resource(RegionListResource, '/regions')

    api.add_resource(ContinentListResource, '/continents')


if __name__ == '__main__':
    app = create_app()
    app.run()
