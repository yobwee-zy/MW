from . import db

#PRODUCT MODEL
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image = db.Column(db.String(200))
    category = db.Column(db.String(50))

#USERS  
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))

    #ORDERS 
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    total = db.Column(db.Float)
    items = db.Column(db.Text)  # Store order items as JSON string

#ORDERS ITEMS
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)