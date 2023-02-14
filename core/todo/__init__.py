from flask import Blueprint

todo = Blueprint("todo", __name__)

from core.todo import routes