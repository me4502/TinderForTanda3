from flask import Flask
from .tinderfortanda import load

app = Flask(__name__)


if __name__ == "__main__":
    load()
    app.run(host='0.0.0.0', port=3000)

