from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ArbitrageForm(FlaskForm):
    odds_a = FloatField('Odds if Team Wins', 
                        validators=[DataRequired(), NumberRange(min=1.01)],
                        default=1.95)
    odds_b = FloatField('Odds if Team Loses', 
                        validators=[DataRequired(), NumberRange(min=1.01)],
                        default=2.16)
    bankroll = FloatField('Bankroll (₹)', 
                          validators=[DataRequired(), NumberRange(min=1)],
                          default=1000)
    submit = SubmitField('Calculate')
