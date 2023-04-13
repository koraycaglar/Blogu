from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/', methods=['GET'])
def hello():
    app.logger.info('Home page viewed')
    data = {'message': 'Selamin Aleykum Ugur.'}
    return jsonify(data)

@app.route('/post', methods=['POST'])
def create_post():
    # Code to create a new blog post
    app.logger.info('New blog post created')
    return 'New blog post created'

@app.route('/login', methods=['POST'])
def login():
    # Code to handle user login
    app.logger.info('User logged in')
    return 'User logged in'

@app.route('/comment', methods=['POST'])
def add_comment():
    # Code to handle user comments
    app.logger.info('New user comment added')
    return 'New user comment added'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

