import flask_blog.controller as controller
from flask import render_template, url_for, redirect, request
from flask_blog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import current_user, logout_user, login_required
from flask import Blueprint


users = Blueprint('users', __name__)

@users.route('/register', methods=['POST', 'GET'])
def register():
    if controller.check_if_user_is_authenticated():
        return redirect(url_for('main.home'))  
    form = RegistrationForm()
    res = controller.create_a_user_of_fail(form)
    if res:
        return redirect(url_for('main.welcome')) 
    else:
        return render_template('users/register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if controller.check_if_user_is_authenticated():
        return redirect(url_for('main.home'))
    form = LoginForm()
    next_page = controller.login_a_user_of_fail(form)
    if next_page:
        return redirect(url_for('main.home'))
    return render_template('users/login.html', title='Login', form=form)



@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.welcome"))

    

@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    controller.edit_account(form)
    if request.method == "GET":
        controller.get_account(form)
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('main/account.html', title='Login', image_file=image_file, form=form)
@users.route('/user/<string:username>')
def user_posts(username):
    page,user,posts = controller.fetch_users_posts(username=username)
    return render_template('users/user_posts.html', posts=posts, user=user,page=page)