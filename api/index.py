from flask import Flask, render_template, request
from app.forms import ArbitrageForm
from app.calculator import is_arbitrage, calculate_stakes
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-for-testing')

# Move templates directory to be found by Flask
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'templates'))
app.template_folder = template_dir

# Move static directory to be found by Flask
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'static'))
app.static_folder = static_dir

@app.route('/', methods=['GET', 'POST'])
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

# For local development
if __name__ == '__main__':
    app.run(debug=True)
    
# For Vercel serverless deployment
app = app
