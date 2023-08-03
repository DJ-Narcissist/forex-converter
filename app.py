from flask import flask, render_template, request, jsonify
from forex_python.converter import CurrencyRates

app = Flask(__name__)
currency_rates = CurrencyRates()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    try:
        rate = currency_rates.get_rate(from_currency, to_currency)
        converted_amount = round(amount * rate, 2)
        return jsonify({'converted_amount': converted_amount})
    except Exception as e :
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)