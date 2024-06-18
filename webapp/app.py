from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

users_data = {
    'test_user': {
        'balance': 0,
        'expenses': []
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addexpense', methods=['POST'])
def add_expense():
    data = request.json
    user_id = 'test_user'
    amount = float(data['amount'])
    description = data['description']
    users_data[user_id]['balance'] -= amount
    users_data[user_id]['expenses'].append({
        'amount': amount,
        'description': description,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return jsonify(success=True)

@app.route('/balance')
def balance():
    user_id = 'test_user'
    balance = users_data[user_id]['balance']
    return jsonify(balance=balance)

@app.route('/history')
def history():
    user_id = 'test_user'
    expenses = users_data[user_id]['expenses']
    return jsonify(expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
