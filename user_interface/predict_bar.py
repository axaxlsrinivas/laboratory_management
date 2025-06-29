import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from flask import Flask, render_template
from app.services.ai_item_model import predict_item_specific_usage

app = Flask(__name__, template_folder='../ui/templates', static_folder='../ui/static')

@app.route('/predict-bar')
def predict_bar():
    # Example items (should be dynamic from DB in production)
    items = [
        {'id': 1, 'name': 'Beaker'},
        {'id': 2, 'name': 'Test Tube'},
        {'id': 3, 'name': 'Microscope'},
        {'id': 4, 'name': 'Bunsen Burner'},
    ]
    day = 5  # Example: predict for day 5
    predictions = []
    for item in items:
        try:
            pred = predict_item_specific_usage(item['id'], day)
        except Exception:
            pred = None
        predictions.append(pred)
    return render_template('predict_bar.html', items=items, predictions=predictions, day=day)

if __name__ == '__main__':
    app.run(debug=True)
