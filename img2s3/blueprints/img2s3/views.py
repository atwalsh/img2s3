from flask import Blueprint, render_template

img2s3_bp = Blueprint('img2s3_bp', __name__)


@img2s3_bp.route('/')
def index():
    return render_template('index.html', app_name='img2s3')