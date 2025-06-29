import unittest
import pandas as pd
from app.services.ai_item_model import train_item_usage_model, predict_item_usage
import os

class TestAIItemModel(unittest.TestCase):
    def setUp(self):
        # Create dummy data for training
        data = pd.DataFrame({
            'item_id': [1, 1, 1, 1],
            'day': [1, 2, 3, 4],
            'used': [10, 12, 13, 15]
        })
        train_item_usage_model(data)

    def tearDown(self):
        # Remove model file after test
        from app.services.ai_item_model import MODEL_PATH
        if os.path.exists(MODEL_PATH):
            os.remove(MODEL_PATH)

    def test_predict_item_usage(self):
        pred = predict_item_usage(5)
        self.assertIsInstance(pred, float)

if __name__ == "__main__":
    unittest.main()
