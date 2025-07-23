from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class SubscriberForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    plan = SelectField('Subscription Plan', choices=[('Basic', 'Basic'), ('Pro', 'Pro'), ('Enterprise', 'Enterprise')], validators=[DataRequired()])
    submit = SubmitField('Subscribe')

class UpdateForm(FlaskForm):
    plan = SelectField('New Plan', choices=[('Basic', 'Basic'), ('Pro', 'Pro'), ('Enterprise', 'Enterprise')], validators=[DataRequired()])
    submit = SubmitField('Update')