from flask import Flask, render_template, url_for, redirect, request
from core.data.session_items import get_items, add_item, remove_item, update_item


from flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())


    from core.main import home as home_bp
    app.register_blueprint(home_bp)

    from core.todo import todo as todo_bp
    app.register_blueprint(todo_bp)

    return app