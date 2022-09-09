from flask import Blueprint, render_template, request
from application.controllers.auth import check_user_login


index_page = Blueprint('index_page', __name__)

@index_page.route("/")
@index_page.route("/index")
def index():
    user_dict = dict()
    session_cookie = request.cookies.get("user-session")

    if session_cookie:
        user_dict = check_user_login(session_cookie)

    return render_template("index.html", user_data=user_dict)
