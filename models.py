"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://images.unsplash.com/photo-1560525821-d5615ef80c69?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"


class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False,)
    last_name = db.Column(db.String(50), nullable=False,)
    image_url = db.Column(db.String(255), nullable=False, default=DEFAULT_IMAGE_URL)


def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

