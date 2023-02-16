from flask import Blueprint

calculator = Blueprint("calculator", __name__)

from core.calculator import routes