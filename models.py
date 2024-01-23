"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://source.unsplash.com/random"


class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text, nullable=False,)
    last_name = db.Column(db.Text, nullable=False,)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts =  db.relationship('Post', backref="user", cascade='all, delete-orphan')

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text, nullable=False,)
    content = db.Column(db.Text, nullable=False,)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    tags = db.relationship('Tag', secondary='post_tags', backref='posts')

class Tag(db.Model):
    """Tag"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

class PostTag(db.Model):
    """PostTag"""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer,
                       db.ForeignKey("posts.id"),
                       primary_key=True)
    tag_id = db.Column(db.Integer,
                          db.ForeignKey("tags.id"),
                          primary_key=True)

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

