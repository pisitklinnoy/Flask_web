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

@app.route("/brand", methods=["GET", "POST"])
def brand():
        return flask.render_template(
            "brand.html",
        )

@app.route("/logout")
@login_required
def logout():
    logout_user()

@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()
    if not form.validate_on_submit():

        return flask.render_template(
            "register.html",
            form=form,
        )
    user = models.User()  # Initialize the user here
    form.populate_obj(user)  # Populate the user object with form data
    role = models.Role.query.filter_by(name="user").first()
    if not role:  # Create the 'user' role if it doesn't exist
        role = models.Role(name="user")
        models.db.session.add(role)
    user.roles.append(role)
    user.password_hash = form.password.data
    models.db.session.add(user)
    models.db.session.commit()
    return flask.redirect(flask.url_for("index"))

    return flask.redirect(flask.url_for("login"))

@app.route("/Porsche", methods=["GET", "POST"])
def Porsche():
        return flask.render_template(
            "porsche.html",
        )

@app.route("/Porsche/porsche_911_GT3_RS", methods=["GET", "POST"])
def porsche_911_GT3_RS():
        return flask.render_template(
            "porsche_911_GT3_RS.html",
        )

@app.route("/Porsche/Porsche_918_Spyder", methods=["GET", "POST"])
def Porsche_918_Spyder():
        return flask.render_template(
            "Porsche_918_Spyder.html",
        )

@app.route("/Lamborghini", methods=["GET", "POST"])
def Lamborghini():
        return flask.render_template(
            "Lamborghini.html",
        )

@app.route("/Lamborghini/Lamborghini_Huracán", methods=["GET", "POST"])
def Lamborghini_Huracán():
        return flask.render_template(
            "Lamborghini_Huracán.html",
        )

@app.route("/Lamborghini/Lamborghini_Reventón", methods=["GET", "POST"])
def Lamborghini_Reventón():
        return flask.render_template(
            "Lamborghini_Reventón.html",
        )
@app.route("/Lamborghini/Lamborghini_Veneno", methods=["GET", "POST"])
def Lamborghini_Veneno():
        return flask.render_template(
            "Lamborghini_Veneno.html",
        )

@app.route("/ferrari", methods=["GET", "POST"])
def Ferrari():
        return flask.render_template(
            "ferrari.html",
        )

@app.route("/ferrari_j50/car", methods=["GET", "POST"])
def ferrari_j50():
        return flask.render_template(
            "ferrari_j50.html",
        )

@app.route("/Ferrari_LaFerrari_Aperta_2016/car", methods=["GET", "POST"])
def Ferrari_LaFerrari_Aperta_2016():
        return flask.render_template(
            "Ferrari_LaFerrari_Aperta_2016.html",
        )

@app.route("/Ferrari_LaFerrari_Coupe_2013/car", methods=["GET", "POST"])
def Ferrari_LaFerrari_Coupe_2013():
        return flask.render_template(
            "Ferrari_LaFerrari_Coupe_2013.html",
        )
if __name__ == "__main__":
    app.run(debug=True)
