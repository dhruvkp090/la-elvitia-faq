from os import environ
from base import app, db

app.run(environ.get('PORT'), debug=True)
