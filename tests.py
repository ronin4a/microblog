from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_password_hashing(self):
    u = User(username='susan')
    u.set_password('cat')
    self.assertFalse(u.check_password('dog'))
    self.assertTrue(u.check_password('cat'))

  def test_follow(self):
    # Declare two users
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')

    # Add the users to db
    db.session.add(u1)
    db.session.add(u2)

    # Commit db
    db.session.commit()

    # Confirm that followed = [], since not initialized yet
    self.assertEqual(u1.followed.all(), [])
    self.assertEqual(u2.followed.all(), [])

    # Update db so john follows susan
    u1.follow(u2)
    db.session.commit()
    self.assertTrue(u1.is_following(u2))
    self.assertEqual(u1.followed.count(), 1)

if __name__=='__main__':
  unittest.main(verbosity=2)
