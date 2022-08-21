from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)
