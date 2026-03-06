from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField, BooleanField, DateField, IntegerRangeField, FloatField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo, Email, Optional, ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import NumberInput


class WarehouseJournalReturn(FlaskForm):
    # element_id = HiddenField()
    # string_field = StringField(render_kw={'disabled': True})
    # text_area_field = TextAreaField(validators=[DataRequired()])
    # number_field = FloatField(
    #     widget     = NumberInput(),
    #     validators = [Optional()],
    #     default    = 0,
	# 	render_kw  = {'readonly': True}
    # )
	pass