from img2s3.config import create_config
from img2s3.app import create_app

config = create_config()
app = create_app(config)

if __name__ == '__main__':
    app.run()
