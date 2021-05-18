from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask('__name__')
db = SQLAlchemy(app,session_options={"expire_on_commit": False})
app.config.from_object('musicapp.config.DevelopmentConfig')

import musicapp.controller
