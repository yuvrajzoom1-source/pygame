import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    return "Bhau Bhau"
app.run()