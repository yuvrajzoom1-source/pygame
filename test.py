import flask
app=flask.Flask(__name__)
@app.route("/<name>")
def index(name):
    return name+" hi noob"
app.run()