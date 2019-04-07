from utilities.logger import Logger
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot-password')
def forgotPwd():
    return render_template('forgot-password.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

if __name__ == "__main__":
    logger = Logger()
    logger.set_basic_config()
    app.run(debug=True)