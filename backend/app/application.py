from flask import Flask, request
from flask_cors import CORS


application = Flask(__name__)
CORS(application)


@application.route('/submission', methods=['GET', 'POST'])
def handle_submission():
    if request.method == 'POST':
        data = request.get_json()
        return data

    elif request.method == 'GET':
        pass


if __name__ == '__main__':
    application.run(debug=True)