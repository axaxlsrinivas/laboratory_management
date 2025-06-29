import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from flask import Flask, render_template, request, redirect, url_for
from app.services.ai_item_model import predict_item_usage, predict_item_specific_usage

app = Flask(__name__, template_folder='../ui/templates', static_folder='../ui/static')

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password123':
            return redirect(url_for('items_list'))
        else:
            message = 'Login failed. Please try again.'
    return render_template('login.html', message=message)

@app.route('/items', methods=['GET', 'POST'])
def items_list():
    items = [
        {'id': 1, 'name': 'Beaker', 'category': 'Glassware', 'quantity': 20},
        {'id': 2, 'name': 'Test Tube', 'category': 'Glassware', 'quantity': 50},
        {'id': 3, 'name': 'Microscope', 'category': 'Equipment', 'quantity': 5},
        {'id': 4, 'name': 'Bunsen Burner', 'category': 'Equipment', 'quantity': 10},
    ]
    day = 5
    if request.method == 'POST':
        try:
            day = int(request.form.get('day', 5))
        except Exception:
            day = 5
    from app.services.ai_item_model import predict_item_specific_usage
    for item in items:
        try:
            item['predicted'] = round(predict_item_specific_usage(item['id'], day), 2)
        except Exception:
            item['predicted'] = 'N/A'
    return render_template('items_list.html', items=items, day=day)

@app.route('/items-ui')
def items_ui():
    return render_template('items_ui.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    error = None
    selected_item = None
    items = [
        {'id': 1, 'name': 'Beaker'},
        {'id': 2, 'name': 'Test Tube'},
        {'id': 3, 'name': 'Microscope'},
        {'id': 4, 'name': 'Bunsen Burner'},
    ]
    if request.method == 'POST':
        try:
            day = int(request.form['day'])
            item_id = int(request.form['item_id'])
            selected_item = item_id
            prediction = predict_item_specific_usage(item_id, day)
        except Exception as e:
            error = str(e)
    return render_template('predict.html', prediction=prediction, error=error, items=items, selected_item=selected_item)

@app.route('/predict-bar', methods=['GET', 'POST'])
def predict_bar():
    items = [
        {'id': 1, 'name': 'Beaker', 'category': 'Glassware'},
        {'id': 2, 'name': 'Test Tube', 'category': 'Glassware'},
        {'id': 3, 'name': 'Microscope', 'category': 'Equipment'},
        {'id': 4, 'name': 'Bunsen Burner', 'category': 'Equipment'},
    ]
    day = 5
    if request.method == 'POST':
        try:
            day = int(request.form.get('day', 5))
        except Exception:
            day = 5
    predictions = []
    for item in items:
        try:
            pred = round(predict_item_specific_usage(item['id'], day), 2)
        except Exception:
            pred = None
        predictions.append(pred)
    labels = [f"{item['name']} ({item['category']})" for item in items]
    return render_template('predict_bar.html', items=items, predictions=predictions, day=day, labels=labels)

if __name__ == '__main__':
    app.run(debug=True)
