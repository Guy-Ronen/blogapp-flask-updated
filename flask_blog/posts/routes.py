import flask_blog.controller as controller
from flask import render_template, url_for, redirect, request
from flask_blog.posts.forms import PostForm
from flask_blog.models import Post
from flask_login import login_required
from flask import Blueprint



posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        controller.add_post(form)
        return redirect(url_for('main.home'))
    else:
        return render_template('posts/create_post.html', title='New Post', form=form, legend="New Post")



@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', post=post)



@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = controller.try_to_fetch_or_abort(post_id=post_id)
    form = PostForm()
    
    if form.validate_on_submit():
        controller.update_post(post=post, form=form)
        return redirect(url_for('main.home', post_id=post.id))
    
    elif request.method == 'GET':
        controller.fetch_post_data(form=form, post=post)
        
    return render_template('posts/create_post.html', 
                           title='Update Post', 
                           form=form,
                           legend='Update Post')
    
    
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    controller.delete_post(post_id=post_id)
    return redirect(url_for('main.home'))









