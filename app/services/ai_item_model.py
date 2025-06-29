import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os
import sys

from app.db.database import get_db_connection

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'item_usage_model.pkl')

def train_item_usage_model(data):
    # data: pandas DataFrame with columns ['item_id', 'day', 'used']
    X = data[['day']]
    y = data['used']
    model = LinearRegression()
    model.fit(X, y)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    return model

def predict_item_usage(day):
    if not os.path.exists(MODEL_PATH):
        raise Exception('Model not trained yet.')
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model.predict([[day]])[0]

def train_model_from_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Example: assumes an 'item_usage' table with columns: item_id, day, used
    cursor.execute('''
        SELECT item_id, day, used FROM item_usage
    ''')
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        raise Exception('No usage data found in the database.')
    data = pd.DataFrame(rows, columns=['item_id', 'day', 'used'])
    return train_item_usage_model(data)

def train_item_specific_model(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT day, used FROM item_usage WHERE item_id = ?
    ''', (item_id,))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        raise Exception(f'No usage data found for item_id {item_id}.')
    data = pd.DataFrame(rows, columns=['day', 'used'])
    X = data[['day']]
    y = data['used']
    model = LinearRegression()
    model.fit(X, y)
    # Save model to a separate file per item
    model_path = os.path.join(os.path.dirname(__file__), f'item_usage_model_{item_id}.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    return model

def predict_item_specific_usage(item_id, day):
    model_path = os.path.join(os.path.dirname(__file__), f'item_usage_model_{item_id}.pkl')
    if not os.path.exists(model_path):
        # Try to train if not exists
        train_item_specific_model(item_id)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model.predict([[day]])[0]
