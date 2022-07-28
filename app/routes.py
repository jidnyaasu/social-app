from app import app


@app.route("/")
@app.route("/index")
def index(name=None):
    return "Hello World!"
