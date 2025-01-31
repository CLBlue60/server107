from flask import Flask, request, jsonify
import json
from http import HTTPStatus

app = Flask(__name__)

# Welcome page on root endpoint
@app.get('/')
def home():
    return "Welcome to the Flask REST API!"

# About page
@app.get('/about')
def about():
    return """
    <h1>About Page</h1>
    <p>This is the about page for the Flask REST API.</p>
    """

# Sample list of products
products = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 20.99},
]

# Get all products
@app.get('/api/product')
def get_products():
    return jsonify(products), HTTPStatus.OK

# Get the number of products in the catalog
@app.get('/api/product/count')
def get_product_count():
    return jsonify({"count": len(products)}), HTTPStatus.OK

# Post a new product
@app.post('/api/product')
def save_product():
    product = request.get_json()
    products.append(product)
    return jsonify({"message": "Product saved!", "product": product}), HTTPStatus.CREATED

# Delete a product by index
@app.delete('/api/product/<int:index>')
def delete_product(index):
    if 0 <= index < len(products):
        deleted_product = products.pop(index)
        return jsonify({"message": "Product deleted!", "product": deleted_product}), HTTPStatus.OK
    else:
        return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND

# Update a product by index
@app.put('/api/product/<int:index>')
def update_product(index):
    product = request.get_json()
    if 0 <= index < len(products):
        products[index] = product
        return jsonify({"message": "Product updated!", "product": product}), HTTPStatus.OK
    else:
        return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

#app.post('/')
#app.put('/')
#app.patch('/')
#app.delete('/')
