from flask import Blueprint

main_test = Blueprint('main', __name__)

from . import views