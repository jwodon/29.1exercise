from models import User, Post, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    User.query.delete()
    Post.query.delete()

    finn = User(first_name='Finn', last_name='ODonnell',
                image_url='https://source.unsplash.com/THi3wQca8Ao')
    rey = User(first_name='Rey', last_name='ODonnell',
                image_url='https://source.unsplash.com/GV2LxPJArgQ')
    barb = User(first_name='Barb', last_name='Kuck',
                image_url='https://source.unsplash.com/NEJcmvLFcws')


    db.session.add_all([finn, rey, barb])
    db.session.commit()

    # Posts
    post1 = Post(title='I love pizza',
                content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum expedita, quo praesentium saepe architecto quae assumenda impedit eveniet recusandae at eum, quod molestias! Totam asperiores nobis ad praesentium numquam accusamus.',
                user=barb)
    post2 = Post(title='What is life',
                content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum expedita, quo praesentium saepe architecto quae assumenda impedit eveniet recusandae at eum, quod molestias! Totam asperiores nobis ad praesentium numquam accusamus.',
                user=finn)
    post3 = Post(title='Ball is bae',
                content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum expedita, quo praesentium saepe architecto quae assumenda impedit eveniet recusandae at eum, quod molestias! Totam asperiores nobis ad praesentium numquam accusamus.',
                user=rey)
    post4 = Post(title='Hello World!',
                content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum expedita, quo praesentium saepe architecto quae assumenda impedit eveniet recusandae at eum, quod molestias! Totam asperiores nobis ad praesentium numquam accusamus.',
                user=barb)
    post5 = Post(title='Gaming for days',
                content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum expedita, quo praesentium saepe architecto quae assumenda impedit eveniet recusandae at eum, quod molestias! Totam asperiores nobis ad praesentium numquam accusamus.',
                user=barb)

    db.session.add_all([post1, post2, post3, post4, post5])
    db.session.commit()

