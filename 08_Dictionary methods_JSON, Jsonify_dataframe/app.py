# Flask Application

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    d = {'left' : 0.1706889, 'right' : 0.98776654, '_unknown_' : 0.98877766}
    message = {
        'status' : 200,
        'message': 'OK',
        'scores' : 'd'
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

    if __name__ == '__main__':
        app.run()