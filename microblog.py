from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Post': Post}

print(app.app_context())
# If running w/out flask command
if __name__=="__main__":
  app.run()
