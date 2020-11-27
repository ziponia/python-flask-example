from flask import Flask, request, jsonify
from datetime import date, datetime

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    data = {
        'version': '1.1',
        'message': 'URL 창에 http://localhost:8080/kuby 로 접속!',
        'requestTime': datetime.today()
    }
    return jsonify(data)


@app.route('/<user_name>', methods=['GET'])
def get_user(user_name):
    data = {
        'user_name': "hello! {}".format(user_name),
        'requestTime': datetime.today()
    }
    return jsonify(data)


if __name__ == "__main__":
    print("서버 시작: {}".format(datetime.today()))
    app.run(host='0.0.0.0', port=8080, debug=True)
