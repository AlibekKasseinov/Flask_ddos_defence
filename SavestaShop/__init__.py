from flask import Flask, render_template, request, url_for, redirect, abort, session
from flask_session import Session
import os

app = Flask(__name__)
sess = Session()

app.config['SECRET_KEY'] = os.urandom(17)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['TEMPLATES_AUTO_RELOAD'] = True
sess.init_app(app)
if __name__=="__main__":
	app.run(hostname='192.168.43.163')