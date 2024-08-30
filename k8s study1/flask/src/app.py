from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host = 'redis', port = 6379)
HOSTNAME = os.environ['HOSTNAME']

@app.route("/")
def index():
    r.incr('visit_count')
    visit_count = r.get('visit_count').decode('utf-8')
    return f"{HOSTNAME}, 방문 횟수: {visit_count}"

