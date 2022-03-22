from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField("Фамилия")
    name = StringField("Имя")
    position = StringField("Профессия")
    address = StringField("Адрес")
    submit = SubmitField('Зарегистрироваться')
    age = IntegerField("Возраст")
    speciality = StringField("Специальность")