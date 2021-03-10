from setuptools import find_packages
from setuptools import setup

setup(
    name='app',
    version='0.0.3',
    description='World API',
    long_description='World API',
    author='Visar Zejnullahu',
    author_email='visar.zejnullahu@gmail.com',
    url='https://github.com/visar/world',
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
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
    project_urls={
        'Changelog': 'https://github.com/visar/world/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/visar/world/issues',
    },
    python_requires='>=3.7',
    license='MIT',
)
