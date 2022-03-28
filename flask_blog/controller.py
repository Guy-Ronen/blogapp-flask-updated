import logging
import secrets
import os
from flask import url_for, flash, redirect, request, abort, current_app
from flask_blog.models import Post, User
from flask_blog import db, bcrypt
from flask_login import login_user, current_user
from logger import get_logger

main_logger = get_logger('main',logging_level=logging.INFO)
users_logger = get_logger('users', logging_level=logging.INFO)
posts_logger = get_logger('posts', logging_level=logging.INFO)


def check_if_user_is_authenticated():
    if current_user.is_authenticated:
        return True
    else:
        return False


def create_a_user_of_fail(form):
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        users_logger.info(f"{user.username} has been created!")
        flash(f"Your account has being created! welcome!, now youre able to log in", 'success')
        return True
    else:
        return False



def login_a_user_of_fail(form):
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            users_logger.info(f"{user.username} has been logged in!")
            flash(f"You have successfully logged in!", 'primary')
            return True
        else:
            users_logger.warning(f"{user.username} has tried to log in unsuccsesfully")
            flash(f"Login Unsuccessful! Check email and password", 'danger')
            return False
    else:
        return 

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picrure_path = os.path.join(current_app.root_path,'static/profile_pics', picture_fn)
    form_picture.save(picrure_path)
    
    return picture_fn


def get_account(form):
    form.username.data = current_user.username
    form.email.data = current_user.email


def edit_account(form):
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        main_logger.info(f"{current_user.username} has successfully updated his account")
        flash("Your account has been successfuly update!", 'success')
        return redirect(url_for('users.account'))

def add_post(form):
    post = Post(title=form.title.data, content=form.content.data, author=current_user)
    db.session.add(post)
    db.session.commit()
    posts_logger.info(f"{current_user.username} has made a post: {post.id}")
    flash('Your post has been created!', 'success')

def update_post(post,form):
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    posts_logger.info(f"{current_user.username} has made a updated his post: {post.id}")
    flash("Your post has been updated!", 'success')


def try_to_fetch_or_abort(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        posts_logger.warning(f"{current_user.username} tried to delete a post that was not his/hers")
        abort(403)
    else:
        return post



def fetch_post_data(form,post):
    form.title.data = post.title
    form.content.data = post.content
    
    
def delete_post(post_id):
    post = try_to_fetch_or_abort(post_id=post_id)
    db.session.delete(post)
    db.session.commit()
    posts_logger.info(f"{current_user.username} has successfully deleted post {post_id}")
    flash("Your post has been deleted!",'success')
    
def fetch_users_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by((Post.date_posted.desc()))\
        .paginate(page=page, per_page=3)
    
    return page,user,posts

def display_home_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3)
    return page,posts
