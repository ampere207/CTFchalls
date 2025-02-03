from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Use the "/read?file=" parameter to read a file.'

@app.route('/read')
def read_file():
    file = request.args.get('file', '')
    if ".." in file or file.startswith('/'):
        return "Unauthorized Access!", 403

    try:
        with open(file, 'r') as f:
            return f.read()
    except:
        return "File not found!", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
