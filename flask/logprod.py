from datetime import datetime
from flask import Flask, request, jsonify
import logging
from kafka import KafkaProducer
import json

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

producer = KafkaProducer(bootstrap_servers='broker:9092',
			value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/', methods=['GET'])
def home():
    app.logger.info('Home page viewed')
    data = {
	'level': 'info',
	'timestamp': datetime.utcnow().isoformat(),
	'endpoint': '/home',
	'ip_address': request.remote_addr,
        'message': 'Home Page Viewed'}
    producer.send('logs', data)
    return 'Home Page'

@app.route('/post', methods=['POST'])
def create_post():
    # Code to create a new blog post
    app.logger.info('New blog post created')
    data = {
        'level': 'info',
        'timestamp': datetime.utcnow().isoformat(),
	'endpoint': '/post',
        'ip_address': request.remote_addr,
        'message': 'New Blog post created'}
    producer.send('logs', data)
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
    app.run(host='0.0.0.0', port=5000)

