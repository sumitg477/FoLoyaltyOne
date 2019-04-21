from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/enterText', methods=['GET'])
def getText1():
    return request.args.get('mirrorText')

@app.route('/frontend', methods=['GET'])
def getText():
    return render_template('WebForm.html')

if __name__ == "__main__":
    app.run()
