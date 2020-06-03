# Coded By Gowtham on 03/06/2020
# Coded Using Visual Studio Code

from flask import Flask, request, jsonify
from BrainyQuotes import getQuotes
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "I_am_Marvelous (^_^)"
CORS(app)


@app.route('/')
def home():
    return 'Quote API is UP!<br><br>A part of <a href="https://t.me/alphaprojects">Alpha Projects</a>'


@app.route('/quotes')
def news():
    if request.method == 'GET':
        category = request.args.get('category')
        return jsonify(getQuotes(category))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
