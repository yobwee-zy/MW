from flask import Blueprint, render_template
from .models import Product

main = Blueprint('main', __name__)

@main.route('/')
def home():
    products = Product.query.limit(6).all()
    return render_template('home.html', products=products)


@main.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)


@main.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)