import functools

from flask import (
    Blueprint, request, current_app
)

### EXAMPLE ###
examples_bp = Blueprint('examples', __name__, url_prefix=current_app.config['API_PREFIX'])
