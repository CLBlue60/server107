from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['product_catalog']  # Database name
products_collection = db['products']  # Collection name

# Root endpoint
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Product Catalog API with MongoDB!"})

# GET /api/catalog endpoint
@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    catalog = list(products_collection.find({}, {'_id': 0}))  # Exclude MongoDB ObjectId from response
    return jsonify(catalog)

# POST /api/catalog endpoint
@app.route('/api/catalog', methods=['POST'])
def add_product():
    product = request.json
    if not product or 'name' not in product or 'price' not in product or 'category' not in product:
        return jsonify({"error": "Invalid product data"}), 400

    # Insert product into MongoDB
    product_id = products_collection.insert_one(product).inserted_id
    return jsonify({"message": "Product added successfully", "product_id": str(product_id)}), 201

# GET /api/reports/total endpoint
@app.route('/api/reports/total', methods=['GET'])
def get_total_value():
    total_value = sum(product['price'] for product in products_collection.find({}))
    return jsonify({"total_value": total_value})

# GET /api/products/<category> endpoint
@app.route('/api/products/<category>', methods=['GET'])
def get_products_by_category(category):
    products = list(products_collection.find({"category": category}, {'_id': 0}))
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
