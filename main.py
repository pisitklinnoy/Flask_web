import flask
import models
import forms
import acl
from flask import flash  # ใช้สำหรับแสดงข้อความแจ้งเตือน
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from flask import Response, send_file, abort, jsonify

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "This is secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

models.init_app(app)

@app.route("/add_favorite", methods=["POST"])
@login_required
def add_favorite():
    if not current_user.is_authenticated:
        return jsonify({"success": False, "error": "User not logged in"}), 401
    
    data = flask.request.get_json()
    car_name = data.get("car_name")
    car_image = data.get("car_image")

    if not car_name:
        return jsonify({"success": False, "error": "Car name is required"}), 400

    new_favorite = models.Favorite(user_id=current_user.id, car_name=car_name, car_image=car_image)
    models.db.session.add(new_favorite)
    models.db.session.commit()

    return jsonify({"success": True, "message": "Car added to favorites"})

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

@app.route("/brand")
def brand():
    if not current_user.is_authenticated:
        flash("Please log in to access this page.", "warning")
        return flask.redirect(flask.url_for("login"))
    return flask.render_template("brand.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("index"))  # กลับไปหน้า index หลัง logout


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

@app.route("/Porsche/Carrera_GT", methods=["GET", "POST"])
def Carrera_GT():
        return flask.render_template(
            "Carrera_GT.html",
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

from flask_login import current_user, login_required

@app.route("/profile")
@login_required
def profile():
    if not current_user.is_authenticated:
        flash("Please log in to access this page.", "warning")  # แจ้งเตือนก่อน redirect
        return flask.redirect(flask.url_for("login"))

    user = current_user
    favorites = models.Favorite.query.filter_by(user_id=user.id).all()
    return flask.render_template("profile.html", user=user, favorites=favorites)



@app.route("/remove_favorite", methods=["POST"])
@login_required
def remove_favorite():
    car_id = flask.request.form.get("car_id")
    favorite = models.Favorite.query.filter_by(id=car_id, user_id=current_user.id).first()

    if favorite:
        models.db.session.delete(favorite)
        models.db.session.commit()

    return flask.redirect(flask.url_for("profile"))


if __name__ == "__main__":
    app.run(debug=True)
