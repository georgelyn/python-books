import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
api_uri = 'http://127.0.0.1:5001'

@app.route('/')
def index():
    response = requests.get(api_uri + '/books').json()
    books = response["books"]
    return render_template('index.html', books=books)

@app.route('/add-book', methods=['GET', 'POST'])
def add():
    if (request.method == 'POST'):
        name = request.form["name"].strip()
        author = request.form["author"].strip()

        response = requests.post(api_uri + '/books', json = { "name": name, 
                                                    "author": author })
        if response.status_code == 500:
            raise
        return redirect('/')
        
    return render_template('add-book.html')

@app.route('/edit-book/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = requests.get(f'{api_uri}/books/{id}').json()

    if (request.method == 'POST'):
        name = request.form["name"].strip()
        author = request.form["author"].strip()

        response = requests.put(api_uri + f'/books/{id}', json = { "name": name, 
                                                    "author": author })
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

