from wtforms import Form, StringField, PasswordField, SelectField, validators
from wtforms.fields.html5 import EmailField, URLField


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(
        min=1, max=50), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(
        min=6, max=50), validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        # Checks that passwords match
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Login Form Class


class LogInForm(Form):
    email = EmailField('Email', [validators.Length(
        min=6, max=50), validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])


# Post Form Class
class PostForm(Form):
    title = StringField('Title', [validators.Length(
        min=1, max=50), validators.DataRequired()])
    description = StringField('Description', [validators.Length(
        min=1, max=50), validators.DataRequired()])
    url = URLField('URL', [validators.DataRequired()])
    difficulty = SelectField(u'Difficulty', choices=[(
        'beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')],
        validators=[validators.DataRequired()])
    category = StringField('Category', [validators.Length(
        min=1, max=50), validators.DataRequired()])
    section = SelectField(u'Section', choices=[(
        'guard', 'Guard'),
        ('passing', 'Passing'),
        ('submissions', 'Submissions'),
        ('defense', 'Defense')],
        validators=[validators.DataRequired()])
