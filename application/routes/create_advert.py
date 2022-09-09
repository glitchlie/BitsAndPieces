from flask import Blueprint, render_template, request, abort, redirect, url_for
from application.controllers.auth import check_user_login
from application.controllers.advert import create_advert


create_advert_page = Blueprint('create_advert_page', __name__)

@create_advert_page.route("/adverts/create", methods=["POST", "GET"])
def create_user_advert():
    user_dict = dict()
    session_cookie = request.cookies.get("user-session")

    if session_cookie:
        user_dict = check_user_login(session_cookie)
    else:
        abort(403)

    form_error_msg = {
            "title_error": "",
            "price_error": ""
    }

    if request.method == "POST":
        request_files = request.files
        
        title = request.form.get("create-adv-title")
        description = request.form.get("create-adv-description")
        price = request.form.get("create-adv-price")

        advert_id = create_advert(user_dict["id"], title, description, price, request_files)
        
        if advert_id:
            return redirect(url_for("user_adverts.adverts"))

    return render_template("create_advert.html", user_data=user_dict)
