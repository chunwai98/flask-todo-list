from flask import render_template, request, url_for, redirect, Blueprint
from flask_login import login_user,logout_user
from main.auth.modules import Users
from main.extensions import bcrypt,db

auth=Blueprint("auth",__name__,template_folder="templates")

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        try:
            user=Users.query.filter(Users.UserName==name).first()         
        except:
            return f"Fail to get User"
        if bcrypt.check_password_hash(user.Passowrd,password):
            login_user(user)
            return redirect(url_for("todos/index"))
    return render_template("login.html")

@auth.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        print(f"{name} {password}")

        if name!=None and password!=None:
            hash_password=bcrypt.generate_password_hash(password)
            user=Users(userName=name,password=hash_password)
            db.session.add(user)
            db.session.commit()
            return f"{Users.__repr__}"
            #return redirect(url_for("login"))
        else:
            return f"Invalid Input"
            
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main/index"))