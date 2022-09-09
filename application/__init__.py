from flask import Flask, make_response, jsonify
import os

from application.routes.index import index_page
from application.routes.register_user import registration_page
from application.routes.login import login_page
from application.routes.logout import logout_page
from application.routes.home_adverts import adverts_page
from application.routes.create_advert import create_advert_page


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(index_page)
app.register_blueprint(registration_page)
app.register_blueprint(login_page)
app.register_blueprint(logout_page)
app.register_blueprint(adverts_page)
app.register_blueprint(create_advert_page)

@app.errorhandler(403)
def custom_403(error):
    return make_response(jsonify({'Response':'Invalid credentials'}), 403)
