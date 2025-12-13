from flask import render_template, request, url_for, redirect,Blueprint
from flask_login import login_user,logout_user,current_user,login_required
from main.todos.modules import Todos
from main.extensions import db

todos=Blueprint("todos",__name__,template_folder="templates")

@todos.route("/",methods=["GET","POST"])
@login_required
def index():
    try:
        todo=Todos.query.all()
        return render_template("index.html",tasks=todo)
    except Exception as e:
        return f"{e}"

@todos.route("/add_task",methods=["GET","POST"])
@login_required
def add_task():
    if request.method=="POST":
        task=request.form.get("task")
        statu=True if "Done" in request.form.keys() else False
        
        todo=Todos(tasks=task,status=statu)
        try:
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            return f"{e}"

    return render_template("add.html")

@todos.route("/update",methods=["POST"])
@login_required
def update(tid):
    task=request.form.get("task")
    statu=request.form.keys()
    try:
        todo=Todos.query.filter(Todos.tid==tid).update(Todos.tasks==task,Todos.status==statu)
        db.session.commit()
    except Exception as e:
        return f"{e}"
    return redirect(url_for("todos/index"))


@todos.route("/delete",methods=["DELETE"])
@login_required
def delete(tid):
    try:
        todo=Todos.query.filter(Todos.tid==tid).delete()
        db.session.commit()
    except Exception as e:
        return f"{e}"
    return redirect(url_for("todos/index"))
