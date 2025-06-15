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


@main.route('/about', methods=['GET'])
def about():
    return jsonify({'message': 'About page'})


@main.route('/contact', methods=['GET'])
def contact():
    return jsonify({'message': 'Contact Details'})


@main.route('/users/insert', methods=['POST'])
def insert_user():
    user_data = request.json
    user_data['id'] = utils.generate_uuid()
    try:
        user = db_adapter.insert_user_data(user_data)
        user = db_adapter.get_user_data(user_data['username'])
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
