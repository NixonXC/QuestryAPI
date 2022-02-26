from flask import Flask
import json, time
import random
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/', methods=['GET'])
@limiter.limit("120/minute")
def home_page():
  lines = open('que.txt').read().splitlines()
  que = random.choice(lines)
  result = que[4:]
  data_set ={'question':result, 'datetime':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
  json_dump = json.dumps(data_set)
  return json_dump

if __name__ == '__main__':
  app.run(debug=True, port='3000', host='0.0.0.0')
