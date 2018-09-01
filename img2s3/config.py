import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
postegres_uri_template = 'postgresql://{}:{}@{}:{}/{}'


class Config:
    def __init__(self):
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.DEBUG = True
        self.ENV = 'development'
        self.ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        # S3 image bucket
        self.image_s3_bucket = os.environ['S3_BUCKET']
        self.image_s3_bucket_key_id = os.environ['S3_KEY_ID']
        self.image_s3_bucket_access_key = os.environ['S3_ACCESS_SECRET']
        self.image_s3_bucket_location = f'https://s3.amazonaws.com/{self.image_s3_bucket}'
        self.image_s3_bucket_folder = os.environ.get('S3_BUCKET_DIR')
        self.port = os.environ.get('PORT', 5000)


def create_config() -> Config:
    return Config()
