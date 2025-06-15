from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from adapters.db_adapter import get_db_model, get_db_session
from sqlalchemy.inspection import inspect
from app import utils

def register_user(user_data):
    # Check if user already exists
    User = get_db_model('User')
    session = get_db_session()
    
    if User.query.filter_by(email=user_data['email']).first():
        session.close()
        return None, "Email already registered"

    # Hash the password
    user_data['password'] = generate_password_hash(user_data['password'])
    user_data['id'] = utils.generate_uuid()
    user_data['created_at'] = utils.get_current_timestamp()
    user_data['updated_at'] = utils.get_current_timestamp()

    # Create new user
    user = User(**user_data)
    session.add(user)
    session.commit()
    
    # Create user dictionary before closing session
    user_dict = {c.key: getattr(user, c.key)
                 for c in inspect(user).mapper.column_attrs}
    
    session.close()
    return user_dict, None

def login_user(email, password):
    User = get_db_model('User')
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        return None, "Invalid email or password"

    # Create access token
    access_token = create_access_token(identity=user.id)
    return access_token, None 