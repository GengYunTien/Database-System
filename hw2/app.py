from flask import Flask
from models import db
from create import create_bp
from read import read_bp
from update import update_bp
from delete import delete_bp
from join import join_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{database}'

db.init_app(app)

app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(join_bp)

if __name__ == '__main__':
    with app.app_context():
        db.session.rollback()
    app.run(debug=True)
