from flask import render_template, request, url_for, redirect, Blueprint
from flask_login import login_user,logout_user
from .forms import LoginForm, SigupForm
from main.auth.modules import Users
from main.extensions import bcrypt,db

auth=Blueprint("auth",__name__,template_folder="templates")

@auth.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if request.method=="POST":
        #if form.validate_on_submit():
            user=Users.query.filter(Users.userName==form.name.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=True)
                return redirect(url_for("todos.index"))
            else:
                 return render_template("login.html",form=form)
    else:
        return render_template("login.html",form=form)


@auth.route("/signup",methods=["GET","POST"])
def signup():
    form=SigupForm()
    if request.method=="POST":
        #if form.validate_on_submit():
            hashed_password=bcrypt.generate_password_hash(form.password.data)
            user=Users(userName=form.name.data,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
    else:
        return render_template("signup.html",form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))