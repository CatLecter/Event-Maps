from dependencies import container
from flask_wtf import FlaskForm
from services.users import UserService
from wtforms import (BooleanField, EmailField, FloatField, PasswordField,
                     StringField, SubmitField, URLField)
from wtforms.validators import DataRequired, EqualTo, ValidationError

user_service: UserService = container.resolve(UserService)


class LoginForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired()], render_kw={'placeholder': 'E-mail'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField(
        'Sign in',
        render_kw={
            'hx-post': '{{ url_for("user.get_profile_by_email") }}',
            'hx-push-url': '{{ url_for("user.get_profile_by_email") }}',
            'hx-swap': 'outerHTML',
        },
    )

    def validate_email(self, email):
        check_email: bool = user_service.check_user_by_email(email=email.data)
        if not check_email:
            raise ValidationError('User with such an email does not exist')


class RegistrationForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()], render_kw={'placeholder': 'Login'})
    email = EmailField('E-mail', validators=[DataRequired()], render_kw={'placeholder': 'E-mail'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    repeat_password = PasswordField(
        'Repeat the password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Repeat the password'},
    )
    full_name = StringField('Full name', validators=[DataRequired()], render_kw={'placeholder': 'Full name'})
    phone = StringField('Phone number', validators=[DataRequired()], render_kw={'placeholder': 'Phone number'})
    photo = URLField('Photo URL', validators=[DataRequired()], render_kw={'placeholder': 'Photo URL'})
    latitude = FloatField('Latitude', validators=[DataRequired()], render_kw={'placeholder': 'Latitude'})
    longitude = FloatField('Longitude', validators=[DataRequired()], render_kw={'placeholder': 'Longitude'})
    submit = SubmitField(
        'Sign up',
        render_kw={
            'hx-post': '{{ url_for("user.add_user") }}',
            'hx-push-url': '{{ url_for("auth.sign_in") }}',
            'hx-swap': 'outerHTML',
        },
    )

    def validate_email(self, email):
        check_email: bool = user_service.check_user_by_email(email=email.data)
        if check_email:
            raise ValidationError('User with such an email already exists')
