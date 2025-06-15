from flask import Blueprint
from app.models import User
from app import utils
from adapters import db_adapter
from adapters.db_adapter import get_db_model, get_db_session
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.auth import register_user, login_user

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return 'Hello, Flask! (Blueprint)'


@main.route('/about')
@jwt_required()
def about():
    return 'About page'


@main.route('/contact')
@jwt_required()
def contact():
    return 'Contact page'


@main.route('/users')
@jwt_required()
def users():
    users = get_db_model('User').query.all()
    return jsonify([user.to_dict() for user in users])


@main.route('/users/insert', methods=['POST'])
def insert_user():
    user_data = request.json
    try:
        user, error = register_user(user_data)
        if error:
            return jsonify({'error': error}), 400
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    access_token, error = login_user(data['email'], data['password'])
    if error:
        return jsonify({'error': error}), 401

    return jsonify({'access_token': access_token}), 200


@main.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({'message': f'Hello user {current_user_id}!'}), 200


@main.route('/users/<user_name>', methods=['GET'])
def get_user(user_name):
    try:
        user = db_adapter.get_user_data(user_name)
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/users/<user_name>', methods=['PUT'])
def update_user(user_name):
    user_data = request.json
    try:
        updated_user = db_adapter.update_user_data(user_name, user_data)
        return jsonify(updated_user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
