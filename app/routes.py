from flask import Blueprint
from app.models import User
from app import utils
from adapters import db_adapter
from adapters.db_adapter import get_db_model, get_db_session
from flask import jsonify, request

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return 'Hello, Flask! (Blueprint)'


@main.route('/about')
def about():
    return 'About page'


@main.route('/contact')
def contact():
    return 'Contact page'


@main.route('/users')
def users():
    users = get_db_model('User').query.all()
    return jsonify([user.to_dict() for user in users])


@main.route('/users/insert', methods=['POST'])
def insert_user():
    user_data = request.json
    user_data['id'] = utils.generate_uuid()
    user = db_adapter.insert_user_data(user_data)
    get_db_session().add(user)
    get_db_session().commit()
    get_db_session().close()
    user = db_adapter.get_user_data(user_data['id'])
    return jsonify({'user_id': user.id})


@main.route('/users/<user_id>')
def update_user(user_id):
    user = get_db_model('User').query.filter_by(id=user_id).first()
    return jsonify(user.to_dict())
