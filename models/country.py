from extensions import db


class Country(db.Model):
    __tablename__ = 'country'
    __table_args__ = (
        db.CheckConstraint(
            "(continent = 'Asia'::text) OR (continent = 'Europe'::text) OR (continent = 'North America'::text) OR (continent = 'Africa'::text) OR (continent = 'Oceania'::text) OR (continent = 'Antarctica'::text) OR (continent = 'South America'::text)"  # noqa
        ),
    )

    code = db.Column(db.String(3),
                     primary_key=True)
    name = db.Column(db.Text,
                     nullable=False)
    continent = db.Column(db.Text,
                          nullable=False)
    region = db.Column(db.Text,
                       nullable=False)
    surfacearea = db.Column(db.Float,
                            nullable=False)
    indepyear = db.Column(db.SmallInteger)
    population = db.Column(db.Integer,
                           nullable=False)
    lifeexpectancy = db.Column(db.Float)
    gnp = db.Column(db.Numeric(10, 2))
    gnpold = db.Column(db.Numeric(10, 2))
    localname = db.Column(db.Text,
                          nullable=False)
    governmentform = db.Column(db.Text,
                               nullable=False)
    headofstate = db.Column(db.Text)
    code2 = db.Column(db.String(2),
                      nullable=False)
    capital = db.Column(db.ForeignKey('city.id'))

    city = db.relationship('City',
                           primaryjoin='Country.capital == City.id',
                           backref='countries')

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_countrycode(cls, country_code):
        return cls.query.filter_by(code=country_code).first()

    @classmethod
    def get_all_by_region(cls, region=None):
        if not region:
            return cls.query.all()
        else:
            return cls.query.filter_by(region=region).all()

    @classmethod
    def get_all_regions_of_continent(cls, continent=None):
        if not continent:
            return cls.query.with_entities(Country.region).distinct().all()
        else:
            return cls.query.filter_by(continent=continent).with_entities(Country.region).distinct().all()

    @classmethod
    def get_continents(cls):
        return cls.query.with_entities(Country.continent).distinct().all()
