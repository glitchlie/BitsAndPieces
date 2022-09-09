from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.controllers.registration import register_user
from application.tools.exceptions import emailExistsError, companyNotRegisteredError


registration_page = Blueprint('registration_page', __name__)

@registration_page.route("/registration", methods=["POST", "GET"])
def user_registration():
    form_error_msg = {
            "email_exists": "",
            "company_not_registered": ""
    }

    if request.method == "POST":
        firstname = request.form.get("reg-input-firstname")
        middlename = request.form.get("reg-input-middlename")
        lastname = request.form.get("reg-input-lastname")
        email = request.form.get("reg-input-email")
        password = request.form.get("reg-input-passwd")
        company = request.form.get("reg-input-company")

        status = register_user(firstname, middlename, lastname, email, password, company)

        if isinstance(status, emailExistsError):
            form_error_msg["email_exists"] = "User with such email exists"
            flash("User with such email exists")
        elif isinstance(status, companyNotRegisteredError):
            form_error_msg["company_not_registered"] = "Company is not registered"
            flash("Company is not registered")
        else:
            print(url_for("index_page.index"))
            return redirect(url_for("index_page.index"))

    return render_template("registration.html", error_msg=form_error_msg)
