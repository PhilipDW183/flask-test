from core.todo import todo
from flask import render_template, url_for, redirect, request
from core.data.session_items import get_items, add_item, remove_item, update_item

base_path = "/todo"

@todo.route(base_path)
def todo_index():
    items = get_items()
    return render_template("todo.html", items=items)

@todo.route(f'{base_path}/create_new_task', methods=["POST"])
def create_new_task():
    new_item = request.form.get('todo')
    add_item(new_item)
    return redirect(url_for("todo.todo_index"))

@todo.route(f'{base_path}/doing_item/<id>')
def doing_item(id):
    update_item(id, "Doing")
    return redirect(url_for("todo.todo_index"))

@todo.route(f'{base_path}/to_do_item/<id>')
def to_do_item(id):
    update_item(id, "Not Started")
    return redirect(url_for("todo.todo_index"))

@todo.route(f'{base_path}/complete_item/<id>')
def complete_item(id):
    update_item(id, "Completed")
    return redirect(url_for("todo.todo_index"))


@todo.route(f'{base_path}/delete_item/<id>')
def delete_item(id):
    remove_item(id)
    return redirect(url_for("todo.todo_index"))