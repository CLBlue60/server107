from flask import Flask
import json


app = Flask(__name__)

@app.get('/')
def home():
    return "Hello from flask!"

@app.get('/test')
def test():
    return "This is another endpoint!"

#this is a json implementation
@app.get('/api/about')
def about():
        name = {"name": "Blue"}
        return json.dumps(name)




app.run(debug=True)

#app.post('/')
#app.put('/')
#app.patch('/')
#app.delete('/')
