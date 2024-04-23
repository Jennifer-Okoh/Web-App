import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

from flask import Flask, request # NOTE: we must import `request` too

app = Flask(__name__)

# Accesing GET request query parameters
# Example 1
# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"

# Example 2
@app.route('/', methods=['POST'])
def post_index():
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return "Not me! :("

# Example 3
@app.route('/', methods=['GET'])
def get_index():
    # RUNS: This route matches! The code inside the block will be executed now.
    return "I am the chosen one!"

# Example 5
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"
# curl "http://localhost:5001/wave?name=Leo"

@app.route('/add-name', methods=['GET'])
def add_names():
    name = request.args['name']
    list_of_names = ['Julia, Alice, Karim']
    return list_of_names.append(name)

# Accesing POST request body paramaters
# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'
    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# Example 4
@app.route('/submit', methods=["POST"])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'
# curl -X POST -d "name=Leo&message=Hello world" http://localhost:5001/submit

@app.route('/count_vowels', methods=["POST"])
def count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number +=1
    return f'There are {vowel_number} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 400
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ','.join(sorted_names)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

