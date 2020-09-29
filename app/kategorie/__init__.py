from flask import Blueprint

bp = Blueprint('kategorie', __name__)

from app.kategorie import routes