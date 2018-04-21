from flask import Flask, send_from_directory
from tinderfortanda import (
    load, get_next_person, get_next_venue, swipe_right, swipe_left
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('client', 'index.html')


@app.route('/get_next_card/:card_type', methods=["GET"])
def get_next_card(card_type=None):
    if card_type == 'user':
        return get_next_person()
    else:
        return get_next_venue()


@app.route('/swipe/:direction/:id', methods=['POST'])
def swipe(direction=None, id=None):
    if direction == 'right':
        return swipe_right(id)
    else:
        return swipe_left(id)

if __name__ == "__main__":
    load()
    app.run(host='0.0.0.0', port=3000)

