from flask import render_template
from app import app
from app.models.order_list import orders

@app.route('/order')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/order/<index>')
def single_order(index):
    chosen_order = orders[int(index)]
    
    return render_template('order.html', order=chosen_order)