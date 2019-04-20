from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/enterText', methods=['GET'])
def getText():
    return request.args.get('mirrorText')

if __name__ == "__main__":
    app.run()

