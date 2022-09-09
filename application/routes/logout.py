from flask import Blueprint, render_template, request, make_response, redirect, url_for
from application.controllers.auth import delete_session


logout_page = Blueprint('logout_page', __name__)

@logout_page.route("/auth/logout")
def logout_action():
    user_dict = dict()
    session_cookie = request.cookies.get("user-session")
    delete_session(session_cookie)

    resp = make_response(redirect(url_for("index_page.index")))
    resp.set_cookie("user-session", "", 0)

    return resp
