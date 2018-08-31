import boto3
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from img2s3.config import create_config

img2s3_bp = Blueprint('img2s3_bp', __name__)

config = create_config()

s3 = boto3.client(
    "s3",
    aws_access_key_id=config.image_s3_bucket_key_id,
    aws_secret_access_key=config.image_s3_bucket_access_key
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    if config.image_s3_bucket_folder:
        f_name = f'{config.image_s3_bucket_folder}/' + file.filename
    else:
        f_name = file.filename

    s3.upload_fileobj(
        file,
        bucket_name,
        f_name,
        ExtraArgs={
            "ACL": acl,
            "ContentType": file.content_type
        }
    )

    return "{}/{}".format(config.image_s3_bucket_location, f_name)


@img2s3_bp.route('/', methods=['GET', 'POST'])
def index():
    urls = None
    if request.method == 'POST':
        urls = []
        files = request.files.getlist("img_file[]")
        for file in files:
            if file and allowed_file(file.filename):
                file.filename = secure_filename(file.filename)
                output = upload_file_to_s3(file, config.image_s3_bucket)
                urls.append(output)
    return render_template('index.html', app_name='img2s3', urls=urls)
