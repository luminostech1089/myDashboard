from utilities.logger import Logger
from flask import Flask, render_template,request

from mydb import AppDb
appDb = AppDb()

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        appDb.connect()
        record = appDb.getUserDetails(email)
        if record and record[1] == pwd:
            return render_template('index.html')
        else:
            return render_template('login.html', error="Incorrect Username or Password!")
    else:
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
    # logger = Logger()
    # logger.set_basic_config()
    from utilities.logger import ConsoleLogger
    ConsoleLogger()
    app.run(debug=True)