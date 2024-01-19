# Import necessary modules
from flask import Flask, render_template, request, jsonify
import colorama

print(colorama.Fore.GREEN + 'Starting Flask server...')

# Create a Flask application
app = Flask(__name__)


# Define a route for handling POST requests
@app.route('/POST', methods=['POST'])
def greet():
    # Get JSON data from the request
    data = request.get_json()

    # Check if 'name' is present in the JSON data
    if 'name' in data:
        name = data['name']

        if name == '':
            return jsonify({'error': 'You must provide a name, you fool'}), 400

        response = {'name': f'Hello, {name}! How are you?'}
        return jsonify(response)

    else:
        # Return an error response if nothing is not provided
        return jsonify({'error': 'You must provide something man...'}), 400


# Define a route for handling GET requests
@app.route('/test', methods=['GET'])
def get():
    # Return a test JSON response
    return jsonify({'test': 'this is a test bro'})


# home screen
@app.route('/')
def home():
    return render_template('index.html')


# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
