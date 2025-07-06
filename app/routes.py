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
    current_user_id = get_jwt_identity()
    user = db_adapter.get_user_data_by_id(current_user_id)
    if not user.get("is_admin", False):
        return jsonify({'error': 'Unauthorized'}), 403
    users = get_db_model('User').query.all()
    return jsonify([user.id for user in users])


@main.route('/insert', methods=['POST'])
def insert_user():
    user_data = request.json
    if "is_admin" not in user_data:
        user_data["is_admin"] = False
    try:
        user, error = register_user(user_data)
        if error:
            return jsonify({'error': error}), 400
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/userprofile', methods=['POST'])
@jwt_required()
def insert_user_profile():
    user_data = request.json
    current_user_id = get_jwt_identity()
    try:
        result = db_adapter.insert_user_profile_data(
            user_data, current_user_id)
        if result.get('error'):
            return jsonify({'error': result.get('error')}), 400
        return jsonify(result)
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
    user = db_adapter.get_user_data_by_id(current_user_id)
    return jsonify(user), 200


@main.route('/users/<user_name>', methods=['GET'])
@jwt_required()
def get_user(user_name):
    current_user_id = get_jwt_identity()
    current_user_is_admin = db_adapter.get_user_data_by_id(
        current_user_id).get("is_admin", False)
    try:
        user = db_adapter.get_user_data(user_name)
        if user.get("id", None) != current_user_id and not current_user_is_admin:
            return jsonify({'error': 'Unauthorized'}), 403
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/users/<user_name>', methods=['PUT'])
@jwt_required()
def update_user(user_name):
    user_data = request.json
    current_user_id = get_jwt_identity()
    current_user_is_admin = db_adapter.get_user_data_by_id(
        current_user_id).get("is_admin", False)
    try:
        user = db_adapter.get_user_data(user_name)
        if user.get("id", None) != current_user_id and not current_user_is_admin:
            return jsonify({'error': 'Unauthorized'}), 403
        updated_user = db_adapter.update_user_data(user_name, user_data)
        return jsonify(updated_user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
