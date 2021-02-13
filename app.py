from flask import Flask, request, jsonify
import os
from summary import summary

# This `app` represents your existing Flask app
app = Flask(__name__)

# An example of one of your Flask app's routes
@app.route("/", methods = ['GET', 'POST'])
def hello():
  content = request.json
  print(content['txt'])
  return summary(content['txt'])


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)
