from flask import Blueprint

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