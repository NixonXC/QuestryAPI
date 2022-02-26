from flask import Flask
import json, time
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
  lines = open('que.txt').read().splitlines()
  que = random.choice(lines)
  result = que[4:]
  data_set ={'question':result, 'datetime':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
  json_dump = json.dumps(data_set)
  return json_dump

if __name__ == '__main__':
  app.run(debug=True, port='3000', host='0.0.0.0')