from ..extensions import db


class CountryLanguage(db.Model):
    __tablename__ = 'countrylanguage'

    countrycode = db.Column(db.ForeignKey('country.code'),
                            primary_key=True,
                            nullable=False)
    language = db.Column(db.Text,
                         primary_key=True,
                         nullable=False)
    isofficial = db.Column(db.Boolean,
                           nullable=False)
    percentage = db.Column(db.Float,
                           nullable=False)

    country = db.relationship(
        'Country', primaryjoin='CountryLanguage.countrycode == Country.code', backref='countrylanguages')

    @classmethod
    def get_by_countrycode(cls, country_code):
        return cls.query.filter_by(countrycode=country_code).all()
