import functools

from flask import (
    Blueprint, request, current_app
)

### WEBHOOK ###
listener_bp = Blueprint('listener', __name__)