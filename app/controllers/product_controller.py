from flask import Blueprint

product_bp = Blueprint('product', __name__)

@product_bp.route('/')
def list_products():
    return "List of products"
