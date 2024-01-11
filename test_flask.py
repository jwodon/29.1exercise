import unittest 
from app import app
from models import db, User

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class BloglyTestCase(unittest.TestCase):

    def setUp(self):
        User.query.delete()
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.session.remove()
        db.drop_all()

    def test_root_redirects_to_users(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/users')

    def test_list_users_route(self):
        response = self.client.get('/users')
        self.assert200(response)

    def test_new_user_form_route(self):
        response = self.client.get('/new')
        self.assert200(response)

    def test_submit_new_user_route(self):
        response = self.client.post('/new', data={'first_name': 'John', 'last_name': 'Doe', 'image_url': 'https://example.com'})
        self.assertRedirects(response, '/users')

    def test_show_user_route(self):
        user = User(first_name='John', last_name='Doe', image_url='https://example.com')
        db.session.add(user)
        db.session.commit()

        response = self.client.get(f'/{user.id}')
        self.assert200(response)


