from flask import Flask, render_template, redirect, url_for, flash, request
from forms import TransactionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

transactions = []

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = {
            'amount': form.amount.data,
            'category': form.category.data,
            'date': form.date.data
        }
        transactions.append(transaction)
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_transaction.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
