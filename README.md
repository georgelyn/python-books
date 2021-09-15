# Books

As a way to familiarize myself with both Python and Flask, I created a simple CRUD web application and API, using SQLite to store the data via the SQLAlchemy ORM library to simplify the DB operations.

![Home page](https://i.imgur.com/FnDZe4B.png)

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

Run the client:

```code
cd app
flask run
```
