"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from markupsafe import Markup, escape



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")

@app.route('/users')
def list_users():
    """Show list of users in the system."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/new', methods=["GET"])
def show_new_user_form():
    """Form to add new user"""
    return render_template('new.html')

@app.route('/new', methods=["POST"])
def submit_new_user():
    """Process new user form submission"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)

@app.route('/edit/<int:user_id>', methods=["GET"])
def show_edit_user_form(user_id):
    """Show form to edit user"""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/edit/<int:user_id>', methods=["POST"])
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

    return redirect("/users")

@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    """Delete user."""
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect("/users")
