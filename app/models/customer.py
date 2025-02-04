from ..db import db, ma
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.isoformat()
        }
    
class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
    
    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    created_at = ma.auto_field()

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)