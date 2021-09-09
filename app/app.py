import requests, base64
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
api_uri = 'http://127.0.0.1:5001'

@app.route('/')
def index():
    try:
        response = requests.get(api_uri + '/books').json()
        books = response["books"]
        return render_template('index.html', books=books)
    except Exception:
        return 'Error: Could not connect to the database' # Error page

@app.route('/add-book', methods=['GET', 'POST'])
def add():
    if (request.method == 'POST'):
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        cover = None

        if 'file' in request.files and request.files['file']:
            file = request.files['file']
            cover = base64.b64encode(file.read()).decode('utf-8')

        response = requests.post(api_uri + '/books', json = { "title": title, 
                                                    "author": author, "cover": cover })
        if response.status_code == 500:
            raise
        return redirect('/')
        
    return render_template('add-book.html')

@app.route('/edit-book/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = requests.get(f'{api_uri}/books/{id}').json()

    if (request.method == 'POST'):
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        cover = None

        if 'file' in request.files and request.files['file']:
            file = request.files['file']
            cover = base64.b64encode(file.read()).decode('utf-8')
        elif 'removeImg' in request.files:
            cover = '';

        response = requests.put(api_uri + f'/books/{id}', json = { "title": title, 
                                                    "author": author, "cover": cover })
        if response.status_code == 500:
            raise
        return redirect('/')

    return render_template('edit-book.html', book=book)


@app.route('/delete-book/<int:id>')
def delete(id):
    response = requests.delete(f'{api_uri}/books/{id}')
    if response.status_code == 500:
        raise
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

