from flask import Flask, render_template, request
from werkzeug.utils import redirect
from data import db_session
from data.users import User
from forms.loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/reg', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db_session.global_init("db/blogs.db")
        user = User()
        user.name = request.form["name"]
        user.surname = request.form["surname"]
        user.address = request.form["address"]
        user.email = request.form["email"]
        user.hashed_password = request.form["password"]
        user.position = request.form["position"]
        user.age = request.form["age"]
        user.speciality = request.form["speciality"]
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('reg.html', form=form, title="а?")


@app.route("/success")
def success():
    return "Форма заполнена"


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
