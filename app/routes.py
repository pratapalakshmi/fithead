from flask import Blueprint
from app.utils import generate_uuid
from app.models import User
from app.adapters.db_adapter import get_db_model, get_db_session
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
    user = get_db_model('User')(
        id=generate_uuid(),
        username=user_data['username'],
        email=user_data['email'],
        age=user_data['age'],
        gender=user_data['gender'],
        location=user_data['location'],
        interests=user_data['interests'],
        bio=user_data['bio'],
    )
    get_db_session().add(user)
    get_db_session().commit()
    return jsonify(user.to_dict())


@main.route('/users/<user_id>')
def update_user(user_id):
    user = get_db_model('User').query.filter_by(id=user_id).first()
    return jsonify(user.to_dict())
