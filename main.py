from flask import Flask

from google.cloud import storage
import google.auth

app = Flask(__name__)

@app.route('/gcs')
def gcs():  
  client = storage.Client()
  buckets = client.list_buckets()
  for bkt in buckets:
    print(bkt)
  return "ok"

@app.route('/')
def hello():
  return "ok"

if __name__ == '__main__':
  
  app.run(host="0.0.0.0", port=8080, debug=False)