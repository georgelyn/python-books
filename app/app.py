import requests, base64
from flask import Flask, render_template, redirect, request, jsonify
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_URL = env.get('API_URL')

@app.route('/')
def index():
    try:
        args = request.args;
        order_by = 'id'
        if 'order_by' in args:
            order_by = args['order_by']

        response = requests.get(f'{API_URL}/books?order_by={order_by}').json()
        books = response['books']
        
        if 'order_by' in args:
            return jsonify({'data': render_template('books.html', books=books)})

        return render_template('index.html', books=books)
    except Exception:
        return redirect('/error')


@app.route('/add-book', methods=['GET', 'POST'])
def add():
    try:
        if (request.method == 'GET'):
            return render_template('add-book.html')

        title = request.form['title'].strip()
        author = request.form['author'].strip()
        cover = None

        if 'file' in request.files and request.files['file']:
            file = request.files['file']
            cover = base64.b64encode(file.read()).decode('utf-8')

        response = requests.post(f'{API_URL}/books', json = { "title": title, 
                                                        "author": author, "cover": cover })

        if response.status_code == 500:
            raise
        return redirect('/')
        
    except Exception:
        return redirect('/error')


@app.route('/book/<int:id>', methods=['GET', 'POST'])
def update(id):
    try:
        if (request.method == 'GET'):
            book = requests.get(f'{API_URL}/books/{id}').json()
            return render_template('edit-book.html', book=book)

        title = request.form['title'].strip()
        author = request.form['author'].strip()
        cover = None

        if 'file' in request.files and request.files['file']:
            file = request.files['file']
            cover = base64.b64encode(file.read()).decode('utf-8')
        elif 'removeImg' in request.files:
            cover = '';

        response = requests.put(f'{API_URL}/books/{id}', json = { "title": title, 
                                                        "author": author, "cover": cover })

        if response.status_code == 500:
            raise
        return redirect('/')
            
    except Exception:
        return redirect('/error')


@app.route('/delete-book/<int:id>')
def delete(id):
    try:
        response = requests.delete(f'{API_URL}/books/{id}')       
        if response.status_code == 500:
            raise
        return redirect('/')
    except Exception:
        return redirect('/error')


@app.route('/error')
def show_error():
    return render_template('error.html');


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

