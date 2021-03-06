from flask import Flask, send_from_directory
from tinderfortanda import (
    load, get_next_person, get_next_venue, swipe_right, swipe_left,
    get_matched_venues, is_venue, get_matched_users
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('client', 'signup.html')


@app.route('/js/<path:filename>', methods=['GET'])
def js(filename=None):
    return send_from_directory('client/js', filename)


@app.route('/css/<path:filename>', methods=['GET'])
def css(filename=None):
    return send_from_directory('client/css', filename)


@app.route('/img/<path:filename>', methods=['GET'])
def img(filename=None):
    return send_from_directory('client/img', filename)


@app.route('/search/jobs', methods=['GET'])
def job_search():
    return send_from_directory('client', 'job_search.html')


@app.route('/search/candidates', methods=['GET'])
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


@app.route('/signup/employee', methods=['GET'])
def signupEmployee():
    return send_from_directory('client', 'signupEmployee.html')


@app.route('/get_next_card/<int:id>', methods=["GET"])
def get_next_card(card_type=None, id=None):
    if is_venue(id):
        return get_next_person(id)
    else:
        return get_next_venue(id)


@app.route('/swipe/<direction>/<int:id>/<int:my_id>', methods=['POST'])
def swipe(direction=None, id=None, my_id=None):
    if direction == 'right':
        return swipe_right(my_id, id)
    else:
        return swipe_left(my_id, id)


@app.route('/get_matched_venues/<int:id>')
def matched_venues(id=None):
    return get_matched_venues(id)


@app.route('/get_matched_users/<int:id>')
def matched_users(id=None):
    return get_matched_users(id)

@app.route('/matches/employer')
def matches_employer():
    return send_from_directory('client', 'matchesEmployer.html')

@app.route('/matches/employee')
def matches_employee():
    return send_from_directory('client', 'matchesEmployee.html')

if __name__ == "__main__":
    load()
    app.run(host='0.0.0.0', port=3000)

