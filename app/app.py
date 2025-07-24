from flask import Flask, render_template, request, redirect, session
import os
from dotenv import load_dotenv
import psycopg2
import logging
from logging.handlers import SysLogHandler
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

# Load environment variables from .env file
load_dotenv('.env')

# Configure logging to syslog
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

syslog_handler = SysLogHandler(address='/dev/log')
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
syslog_handler.setFormatter(formatter)
logger.addHandler(syslog_handler)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('db_host'),
        database=os.getenv('db_name'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password')
    )


@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect('/login')


def get_client_ip():
    return request.remote_addr


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session['user'] = username
            logger.warning(f"[LOGIN SUCCESSFUL] username={username}, ip={get_client_ip()}")
            return redirect('/')
        else:
            logger.warning(f"[LOGIN FAIL] username={username}, ip={get_client_ip()}")
            error = "Incorrect username or password"
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
