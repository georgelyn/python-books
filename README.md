# Books

As a way to familiarize myself with both Python and Flask, I created a simple CRUD web application and API, using SQLite to store the data via the SQLAlchemy ORM library to simplify the DB operations.

![Home page](https://i.imgur.com/63qfHq1.png)

![Add page](https://i.imgur.com/znOLFnf.png)

## Setup and installation

After cloning the repository, create and activate a virtual environment, and install the requirements:

```code
cd python-books
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

You must run both the client and the API. From the root directory:

Run the API:

```code
cd api
flask run
```

You can access it by going to [http://127.0.0.1:5001/](http://127.0.0.1:5001/)

Run the client:

```code
cd app
flask run
```

You can access it by going to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
