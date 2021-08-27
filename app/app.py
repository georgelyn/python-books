import requests
from flask import Flask, render_template

app = Flask(__name__)
api_uri = 'http://127.0.0.1:5001'

@app.route('/')
def index():
    response = requests.get(api_uri + '/books').json()
    books = response["books"]
    return render_template('index.html', books=books)

@app.route('/add-book')
def add():
    return render_template('book.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

