import functools

from flask import (
    Blueprint, request, current_app
)

### WEBHOOK ###
webhook_bp = Blueprint('webhook', __name__, url_prefix=current_app.config['API_PREFIX'])
