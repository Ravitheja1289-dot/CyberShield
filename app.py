from flask import Flask, render_template, request,jsonify
from mail import result

app = Flask(__name__)

@app.route('/get_res')
def get_res():
    data=result
    return jsonify(data)
@app.route('/')
def home():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)