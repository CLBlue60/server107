from flask import Flask, jsonify
from routes.product_routes import product_routes
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, disables CORS policy (WARNING)



# MongoDB collection
products_collection = db['products']  # Collection name

# Root endpoint
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Product Catalog API with MongoDB!"})

# Register blueprints
app.register_blueprint(product_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
