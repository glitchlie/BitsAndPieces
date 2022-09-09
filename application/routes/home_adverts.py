from flask import Blueprint, render_template, request
from application.controllers.auth import check_user_login
from application.controllers.advert import get_user_adverts


adverts_page = Blueprint('user_adverts', __name__)

@adverts_page.route("/home/adverts")
def adverts():
    user_dict = dict()
    session_cookie = request.cookies.get("user-session")

    if session_cookie:
        user_dict = check_user_login(session_cookie)
    else:
        abort(403)

    adverts = get_user_adverts(user_dict["id"])
    print(adverts)

    adverts_data = [{"title": item[1], 
                     "price": item[2],
                     "images": item[3]} for item in adverts]
    
    print(adverts_data)

    return render_template("home_adverts.html", adverts_data=adverts_data)
