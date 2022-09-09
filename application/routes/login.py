from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response
from application.controllers.auth import login_user
from application.tools.exceptions import emailExistsError, userNotExistsError, companyNotRegisteredError, wrongUserPassword
from application.tools.generators import generate_cookie_str


login_page = Blueprint('login_page', __name__)

@login_page.route("/auth/login", methods=["POST", "GET"])
def user_login():
    form_error_msg = {
            "login_error": ""
    }

    if request.method == "POST":
        email = request.form.get("login-input-email")
        password = request.form.get("login-input-passwd")

        session_cookie = generate_cookie_str(128)

        status = login_user(session_cookie, email, password)

        if isinstance(status, userNotExistsError):
            form_error_msg["login_error"] = "Пользователя с такой почтой не существует"
        elif isinstance(status, wrongUserPassword):
            form_error_msg["login_error"] = "Неправильный логин/пароль"
        else:
            resp = make_response(redirect(url_for("index_page.index")))
            resp.set_cookie("user-session", session_cookie, 60*60*24)
            return resp

    return render_template("login.html", error_msg=form_error_msg)
