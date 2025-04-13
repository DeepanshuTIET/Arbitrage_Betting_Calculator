from flask import Blueprint, render_template, request, flash
from app.forms import ArbitrageForm
from app.calculator import is_arbitrage, calculate_stakes

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ArbitrageForm()
    result = None
    has_arbitrage = False
    
    if form.validate_on_submit():
        odds_a = form.odds_a.data
        odds_b = form.odds_b.data
        bankroll = form.bankroll.data
        
        has_arbitrage = is_arbitrage(odds_a, odds_b)
        
        if has_arbitrage:
            result = calculate_stakes(odds_a, odds_b, bankroll)
        
    return render_template('index.html', form=form, result=result, has_arbitrage=has_arbitrage)
