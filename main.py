import flask
import models
import forms
import acl

from flask_login import login_required, login_user, logout_user
from flask import Response, send_file, abort

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "This is secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

models.init_app(app)


@app.route("/")
def index():
    db = models.db
    notes = db.session.execute(
        db.select(models.Note).order_by(models.Note.title)
    ).scalars()
    return flask.render_template(
        "index.html",
        notes=notes,
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()

    if not form.validate_on_submit():
        return flask.render_template(
            "login.html",
            form=form,
        )
    user = models.User.query.filter_by(username=form.username.data).first()

    if user and user.authenticate(form.password.data):
        login_user(user)
        return flask.redirect(flask.url_for("index"))
    return flask.redirect(flask.url_for("login", error="Invalid username or password"))

if __name__ == "__main__":
    app.run(debug=True)
