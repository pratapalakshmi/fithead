from flask_sqlalchemy import SQLAlchemy
from app import models
from app import utils
import time
from sqlalchemy.inspection import inspect

db = SQLAlchemy()


def get_db_model(model_name):
    return getattr(models, model_name)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def get_db():
    return db


def get_db_session():
    return db.session


def get_db_engine():
    return db.engine


def insert_user_data(user_data):
    user = models.User(
        id=user_data['id'],
        username=user_data['username'],
        email=user_data['email'],
        age=user_data['age'],
        gender=user_data['gender'],
        location=user_data['location'],
        interests=user_data['interests'],
        bio=user_data['bio'],
        profile_picture=user_data['profile_picture'],
        created_at=utils.get_current_timestamp(),
        updated_at=utils.get_current_timestamp(),
    )
    get_db_session().add(user)
    get_db_session().commit()
    get_db_session().close()
    return user


def insert_workout_data(workout_data):
    workout = models.Workout(
        id=workout_data['id'],
        user_id=workout_data['user_id'],
        workout_type=workout_data['workout_type'],
        workout_name=workout_data['workout_name'],
    )


def insert_workout_plan_data(workout_plan_data):
    workout_plan = WorkoutPlan(
        id=workout_plan_data['id'],
        user_id=workout_plan_data['user_id'],
        workout_plan_name=workout_plan_data['workout_plan_name'],
    )


def insert_workout_plan_exercise_data(workout_plan_exercise_data):
    workout_plan_exercise = models.WorkoutPlanExercise(
        id=workout_plan_exercise_data['id'],
        workout_plan_id=workout_plan_exercise_data['workout_plan_id'],
        exercise_name=workout_plan_exercise_data['exercise_name'],
    )


def get_user_data(user_name):
    user = models.User.query.filter_by(username=user_name).first()
    user_dict = {c.key: getattr(user, c.key)
                 for c in inspect(user).mapper.column_attrs}
    return user_dict


def update_user_data(user_name, user_data):
    user = models.User.query.filter_by(username=user_name).first()
    for key, value in user_data.items():
        setattr(user, key, value)
    user.updated_at = utils.get_current_timestamp()
    get_db_session().add(user)
    get_db_session().commit()
    get_db_session().close()
    user = models.User.query.filter_by(username=user_name).first()
    user_dict = {c.key: getattr(user, c.key)
                 for c in inspect(user).mapper.column_attrs}
    return user_dict


def get_workout_data(workout_id):
    workout = models.Workout.query.filter_by(id=workout_id).first()
    return workout


def get_workout_plan_data(workout_plan_id):
    workout_plan = models.WorkoutPlan.query.filter_by(
        id=workout_plan_id).first()
    return workout_plan


def get_workout_plan_exercise_data(workout_plan_exercise_id):
    workout_plan_exercise = models.WorkoutPlanExercise.query.filter_by(
        id=workout_plan_exercise_id).first()
    return workout_plan_exercise


def close_db(e=None):
    db.session.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    init_db(app)
    return db
