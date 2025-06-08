from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Example model


def default_repr(self): return f"<{self.__class__.__name__} id={self.id}>"


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    interests = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    __repr__ = default_repr


class Workout(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey(
        'user.id'), nullable=False)
    workout_type = db.Column(db.String(120), nullable=False)
    workout_name = db.Column(db.String(120), nullable=False)
    workout_description = db.Column(db.String(255), nullable=False)
    workout_reps = db.Column(db.Integer, nullable=False)
    workout_sets = db.Column(db.Integer, nullable=False)
    workout_weight = db.Column(db.Float, nullable=False)
    workout_date = db.Column(db.DateTime, nullable=False)
    workout_duration = db.Column(db.Integer, nullable=False)
    workout_calories = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    __repr__ = default_repr


class WorkoutPlan(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey(
        'user.id'), nullable=False)
    workout_plan_name = db.Column(db.String(120), nullable=False)
    workout_plan_description = db.Column(db.String(255), nullable=False)
    workout_plan_exercises = db.Column(db.String(255), nullable=False)
    workout_plan_duration = db.Column(db.Integer, nullable=False)
    workout_plan_calories = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    __repr__ = default_repr


class WorkoutPlanExercise(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    workout_plan_id = db.Column(db.String(36), db.ForeignKey(
        'workout_plan.id'), nullable=False)
    exercise_name = db.Column(db.String(120), nullable=False)
    exercise_description = db.Column(db.String(255), nullable=False)
    exercise_reps = db.Column(db.Integer, nullable=False)
    exercise_sets = db.Column(db.Integer, nullable=False)
    exercise_weight = db.Column(db.Float, nullable=False)
    exercise_duration = db.Column(db.Integer, nullable=False)
    exercise_calories = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    __repr__ = default_repr
