from flask import Flask, send_from_directory
from tinderfortanda import (
    load, get_next_person, get_next_venue, swipe_right, swipe_left
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('client', 'index.html')

@app.route('/search/jobs', methods=['GET'])
def job_search():
    return send_from_directory('client', 'job_search.html')

@app.route('/search/candiates', methods=['GET'])
def candidate_search():
    return send_from_directory('client', 'candidate_search.html')

@app.route('/profile/employee', methods=['GET'])
def profileEmployee():
    return send_from_directory('client', 'profileEmployee.html')

@app.route('/profile/employer', methods=['GET'])
def profileEmployer():
    return send_from_directory('client', 'profileEmployer.html')

@app.route('/signup', methods=['GET'])
def signup():
    return send_from_directory('client', 'signup.html')

@app.route('/signup/employer', methods=['GET'])
def signupEmployer():
    return send_from_directory('client', 'signupEmployer.html')

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

