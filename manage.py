from flask_migrate import MigrateCommand
from flask_script import Manager

from img2s3.app import create_app
from img2s3.config import create_config

app = create_app(config=create_config())

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
