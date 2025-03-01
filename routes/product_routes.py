from flask import Blueprint, jsonify, request
from config import db  # Import the database connection
from bson.objectid import ObjectId  # For handling MongoDB ObjectId

product_routes = Blueprint('product_routes', __name__)

# MongoDB collections
products_collection = db['products']
coupons_collection = db['coupons']

# GET /api/products endpoint
@product_routes.route('/products', methods=['GET'])
def get_products():
    try:
        # Include _id in the response and convert it to a string
        products = list(products_collection.find({}))
        for product in products:
            product['_id'] = str(product['_id'])  # Convert ObjectId to string
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /api/products endpoint
@product_routes.route('/products', methods=['POST'])
def save_product():
    try:
        product = request.json
        if not product or 'title' not in product or 'price' not in product or 'category' not in product:
            return jsonify({"error": "Invalid product data"}), 400

        # Ensure the product doesn't already exist (optional)
        existing_product = products_collection.find_one({"title": product['title']})
        if existing_product:
            return jsonify({"error": "Product with the same title already exists"}), 400

        # Insert product into MongoDB
        product_id = products_collection.insert_one(product).inserted_id
        return jsonify({"message": "Product added successfully", "product_id": str(product_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/reports/total endpoint
@product_routes.route('/reports/total', methods=['GET'])
def get_total_value():
    try:
        total_value = sum(product['price'] for product in products_collection.find({}))
        return jsonify({"total_value": total_value})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/products/<category> endpoint
@product_routes.route('/products/<category>', methods=['GET'])
def get_products_by_category(category):
    try:
        products = list(products_collection.find({"category": category}))
        for product in products:
            product['_id'] = str(product['_id'])  # Convert ObjectId to string
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/coupons endpoint
@product_routes.route('/coupons', methods=['GET'])
def get_coupons():
    try:
        coupons = list(coupons_collection.find({}))
        for coupon in coupons:
            coupon['_id'] = str(coupon['_id'])  # Convert ObjectId to string
        return jsonify(coupons)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /api/coupons endpoint
@product_routes.route('/coupons', methods=['POST'])
def save_coupon():
    try:
        coupon = request.json
        if not coupon or 'code' not in coupon or 'discount' not in coupon:
            return jsonify({"error": "Invalid coupon data"}), 400

        # Ensure the coupon code is unique
        existing_coupon = coupons_collection.find_one({"code": coupon['code']})
        if existing_coupon:
            return jsonify({"error": "Coupon with the same code already exists"}), 400

        # Insert coupon into MongoDB
        coupon_id = coupons_collection.insert_one(coupon).inserted_id
        return jsonify({"message": "Coupon added successfully", "coupon_id": str(coupon_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
