from flask import request

from ..service.event_service import parse_event

from ..manage import app

print('hi')
print(app)

@app.route('/')
def hello():
    return "Hello World!"