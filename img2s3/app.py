from flask import Flask

from .blueprints import img2s3_bp


def create_app(config=None, app_name=None):
    """
    Create a Flask app.
    :param config: A Config type object for configuring the application.
    :param app_name: The name of the app.
    :return: The Flask app instance.
    """
    if config is None:
        raise Exception('No configuration passed to create_app().')
    if app_name is None:
        app_name = 'img2s3'

    app = Flask(app_name)

    configure_app(app, config)
    configure_blueprints(app)
    return app


def configure_app(app: Flask, config):
    """
    Configure the app.
    :param app: A Flask app.
    :param config: A config object.
    """
    app.config.from_object(config)


def configure_blueprints(app: Flask):
    """
    Configure blueprints.
    """
    app.register_blueprint(img2s3_bp)
