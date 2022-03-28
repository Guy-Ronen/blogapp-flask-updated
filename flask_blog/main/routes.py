import flask_blog.controller as controller
from flask import flash, render_template, url_for, redirect
from flask import Blueprint
from flask_blog.controller import main_logger

main = Blueprint('main', __name__)


@main.route('/')
def welcome():
    if controller.check_if_user_is_authenticated():
        main_logger.warning('User tried to see landing page while logged in')
        return redirect(url_for('main.home')) 
    return render_template('main/landing_page.html')


@main.route('/home', methods=['GET'])
def home():
    if not controller.check_if_user_is_authenticated():
        flash('Please Register or Login to see posts!','danger')
        main_logger.warning('User tried to see posts without being authenticated!')
        return redirect(url_for('main.welcome')) 
    page,posts = controller.display_home_posts()
    return render_template('main/home.html', posts=posts, page=page)

@main.route('/about')
def about():
    return render_template('main/about.html', title='About')