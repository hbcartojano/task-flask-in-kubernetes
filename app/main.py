import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/healthy')
def health_check():
    return 'OK'

@app.route('/config')
def config():
    return jsonify({"DEBUG": app.config['DEBUG']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
