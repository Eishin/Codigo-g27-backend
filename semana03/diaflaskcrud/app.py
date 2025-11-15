from flask import flask, request

app = flask(__name__)

new_users = {
    'id': 1,
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'password': 'password'
}

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/users', methods=['GET', 'POST'])
def users():
    method = request.method
    if method == 'GET':
        pass
    elif method == 'POST':
        pass

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def users(id):
    method = request.method
    if method == 'GET':
        pass
    elif method == 'PUT':
        pass
    elif method == 'DELETE':
        pass
    
if __name__ == '__main__':
    app.run(debug=True)

