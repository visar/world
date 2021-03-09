from flask import Flask
from flask_restful import Api

from config import Config
from extensions import db
from resources.city import CityListResource
from resources.city import CityResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_resources(app):
    api = Api(app)

    api.add_resource(CityListResource, '/cities')
    api.add_resource(CityResource, '/cities/<int:city_id>')


if __name__ == '__main__':
    app = create_app()
    app.run()
