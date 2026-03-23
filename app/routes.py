from flask import Blueprint, render_template
from .models import Product

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@main.route('/cart')
def cart():
    return render_template('cart.html')

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)



#     category = request.args.get('category')
#     search = request.args.get('search')

#     query = Product.query

#     # Filter by category
#     if category and category != "All":
#         query = query.filter(Product.category == category)

#     # Search by name
#     if search:
#         query = query.filter(Product.name.ilike(f"%{search}%"))

#     products = query.all()

#     # Get unique categories
#     categories = db.session.query(Product.category).distinct().all()
#     categories = [c[0] for c in categories]

#     return render_template(
#         'shop.html',
#         products=products,
#         categories=categories,
#         selected_category=category,
#         search=search
#     )


# @main.route('/product/<int:id>')
# def product(id):
#     product = Product.query.get_or_404(id)
#     return render_template('product.html', product=product)