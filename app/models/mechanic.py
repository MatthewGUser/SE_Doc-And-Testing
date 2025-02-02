from ..db import db, ma

class Mechanic(db.Model):
    __tablename__ = 'mechanics'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Fixed uni1 to unique
    specialty = db.Column(db.String(100))

class MechanicSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Mechanic
    
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    specialty = ma.auto_field()

mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)