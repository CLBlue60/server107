from flask import Blueprint, jsonify, request
from config import db  # Import the database connection

product_routes = Blueprint('product_routes', __name__)

# MongoDB collections
products_collection = db['products']  
coupons_collection = db['coupons']

# GET /api/products endpoint
@product_routes.route('/products', methods=['GET'])
def get_products():
    products = list(products_collection.find({}, {'_id': 0}))
    return jsonify(products)

# POST /api/products endpoint
@product_routes.route('/products', methods=['POST'])
def save_product():
    product = request.json
    if not product or 'title' not in product or 'price' not in product or 'category' not in product:
        return jsonify({"error": "Invalid product data"}), 400

    # Insert product into MongoDB
    product_id = products_collection.insert_one(product).inserted_id
    return jsonify({"message": "Product added successfully", "product_id": str(product_id)}), 201

# GET /api/reports/total endpoint
@product_routes.route('/reports/total', methods=['GET'])
def get_total_value():
    total_value = sum(product['price'] for product in products_collection.find({}))
    return jsonify({"total_value": total_value})

# GET /api/products/<category> endpoint
@product_routes.route('/products/<category>', methods=['GET'])
def get_products_by_category(category):
    products = list(products_collection.find({"category": category}, {'_id': 0}))
    return jsonify(products)

# GET /api/coupons endpoint
@product_routes.route('/coupons', methods=['GET'])
def get_coupons():
    coupons = list(coupons_collection.find({}, {'_id': 0}))
    return jsonify(coupons)

# POST /api/coupons endpoint
@product_routes.route('/coupons', methods=['POST'])
def save_coupon():
    coupon = request.json
    if not coupon or 'code' not in coupon or 'discount' not in coupon:
        return jsonify({"error": "Invalid coupon data"}), 400

    # Insert coupon into MongoDB
    coupon_id = coupons_collection.insert_one(coupon).inserted_id
    return jsonify({"message": "Coupon added successfully", "coupon_id": str(coupon_id)}), 201
