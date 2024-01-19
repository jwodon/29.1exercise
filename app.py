"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
from markupsafe import Markup, escape



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users/users")

@app.route('/users/users')
def list_users():
    """Show list of users in the system."""
    users = User.query.all()
    return render_template('users/users.html', users=users)

@app.route('/users/new', methods=["GET"])
def show_new_user_form():
    """Form to add new user"""
    return render_template('users/new.html')

@app.route('/users/new', methods=["POST"])
def submit_new_user():
    """Process new user form submission"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users/users")

@app.route("/users/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("users/detail.html", user=user)

@app.route('/users/edit/<int:user_id>', methods=["GET"])
def show_edit_user_form(user_id):
    """Show form to edit user"""
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/edit/<int:user_id>', methods=["POST"])
def edit_user(user_id):
    """Process updated user info form submission"""
    new_first_name = request.form['first_name']
    new_last_name = request.form['last_name']
    new_image_url = request.form['image_url']

    user_to_update = User.query.get_or_404(user_id)

    user_to_update.first_name = new_first_name
    user_to_update.last_name = new_last_name
    user_to_update.image_url = new_image_url

    db.session.commit()

    return redirect("/users/users")

@app.route('/users/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    """Delete user."""
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect("/users/users")

@app.route('/posts/new_post/<int:user_id>', methods=["GET"])
def show_new_post_form(user_id):
    """Form to add new post"""
    user = User.query.get_or_404(user_id)
    return render_template('posts/new_post.html', user=user)

@app.route('/posts/new_post/<int:user_id>', methods=["POST"])
def submit_new_post(user_id):
    """Process new post form submission"""
    title = request.form['title']
    content = request.form['content']
    user_id=user_id

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect("/users/users")

@app.route("/posts/detail_post/<int:post_id>")
def show_post(post_id):
    """Show info on a single user."""

    post = Post.query.get_or_404(post_id)
    user = post.user
    return render_template("posts/detail_post.html", post=post, user=user)

@app.route('/posts/detail_post/<int:post_id>', methods=["POST"])
def delete_post(post_id):
    """Delete post."""
    post_to_delete = Post.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect("/users/users")

@app.route('/posts/edit_post/<int:post_id>', methods=["GET"])
def show_edit_post_form(post_id):
    """Show form to edit post"""
    post = Post.query.get_or_404(post_id)
    return render_template('posts/edit_post.html', post=post)

@app.route('/posts/edit_post/<int:post_id>', methods=["POST"])
def edit_post(post_id):
    """Process updated post form submission"""
    new_title = request.form['title']
    new_content = request.form['content']

    post_to_edit = Post.query.get_or_404(post_id)

    post_to_edit.title = new_title
    post_to_edit.content = new_content

    db.session.commit()

    return redirect("/users/users")


