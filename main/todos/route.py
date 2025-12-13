from flask import render_template, request, url_for, redirect,Blueprint
from flask_login import login_user,logout_user,current_user,login_required
from .forms import TodoForm
from main.todos.modules import Todos
from main.extensions import db

todos=Blueprint("todos",__name__,template_folder="templates")

@todos.route("/index",methods=["GET","POST"])
@login_required
def index():
    try:
        todo=Todos.query.all()
        return render_template("todo_index.html",todo=todo)
    except Exception as e:
        db.session.rollback()
        return f"{e}"

@todos.route("/add_task",methods=["GET","POST"])
@login_required
def add_task():
    form=TodoForm()
    if request.method=="POST":
        task=form.task.data
        completed=form.completed.data
        todo=Todos(tasks=task,completed=completed)
        try:
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"{e}"
        return redirect(url_for("todos.index"))
    return render_template("add_task.html",form=form)

@todos.route("/update/<tid>")
@login_required
def update(tid):
    try:
        todo = Todos.query.filter_by(tid=tid).first()
        if not todo:
            return "Todo not found", 404
        todo.completed = not todo.completed
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return str(e), 500
    return redirect(url_for("todos.index"))
"""
def update(tid):
    try:
        Todos.query.filter(Todos.tid==tid).update(values={Todos.completed: False if Todos.completed else True})
        db.session.commit()
    except Exception as e:
        return f"{e}"
    return redirect(url_for("todos.index"))
"""

@todos.route("/delete/<tid>")
@login_required
def delete(tid):
    try:
        todo=Todos.query.filter(Todos.tid==tid).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"{e}"
    return redirect(url_for("todos.index"))
