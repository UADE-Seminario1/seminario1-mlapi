from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)


bp = Blueprint('api', __name__)

@bp.route("/")
def get_health():
    info = dict(
        status='OK'
    )

    return jsonify(info)



