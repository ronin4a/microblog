from app import db
from app.models import User, Post

def add_user(name, email_address):
  u = User(username=name, email=email_address)
  db.session.add(u)
  db.session.commit()

def main():
  add_user('john', 'john@example.com')
  add_user('susan', 'susan@example.com')

  users = User.query.all()

  print(users)

if __name__=="__main__":
  main()
