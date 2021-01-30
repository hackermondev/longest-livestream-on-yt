import flask
import threading

from flask import *

app = flask.Flask('hi')

@app.route('/')
def home():
  return "hi"

def thread():
  app.run(host="0.0.0.0", port="3000")

t = threading.Thread(target=thread)

t.start()