from extensions import db


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    countrycode = db.Column(db.String(3), nullable=False)
    district = db.Column(db.Text, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, city_id):
        return cls.query.filter_by(id=city_id).first()

    @classmethod
    def get_by_countrycode(cls, country_code):
        return cls.query.filter_by(countrycode=country_code).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
