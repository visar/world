from setuptools import find_packages
from setuptools import setup

setup(
    name='app',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-caching',
        'flask-restful',
        'flask-sqlalchemy',
        'marshmallow',
        'psycopg2-binary',
        'webargs',
    ],
)
