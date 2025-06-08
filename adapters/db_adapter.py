from flask_sqlalchemy import SQLAlchemy
from app.models import User, Workout, WorkoutPlan, WorkoutPlanExercise

db = SQLAlchemy()


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


def get_db_model(model_name):
    return getattr(db, model_name)


def insert_user_data(user_data):
    user = User(
        id=user_data['id'],
        username=user_data['username'],
        email=user_data['email'],
        age=user_data['age'],
    )


def insert_workout_data(workout_data):
    workout = Workout(
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
    workout_plan_exercise = WorkoutPlanExercise(
        id=workout_plan_exercise_data['id'],
        workout_plan_id=workout_plan_exercise_data['workout_plan_id'],
        exercise_name=workout_plan_exercise_data['exercise_name'],
    )


def get_user_data(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


def get_workout_data(workout_id):
    workout = Workout.query.filter_by(id=workout_id).first()
    return workout


def get_workout_plan_data(workout_plan_id):
    workout_plan = WorkoutPlan.query.filter_by(id=workout_plan_id).first()
    return workout_plan


def get_workout_plan_exercise_data(workout_plan_exercise_id):
    workout_plan_exercise = WorkoutPlanExercise.query.filter_by(
        id=workout_plan_exercise_id).first()
    return workout_plan_exercise


def close_db(e=None):
    db.session.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    init_db(app)
    return db
