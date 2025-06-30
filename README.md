# Laboratory Management System

A modern, educational, and extensible Laboratory Management System for tracking laboratory items, predicting usage with AI, and providing both web and CLI interfaces. Designed for students, developers, and educators to learn, extend, and manage laboratory resources efficiently.

---

## Project Overview

This project provides a full-stack solution for laboratory inventory management, including:
- **User login** (demo credentials: `admin` / `password123`)
- **Item management**: View, track, and predict usage of laboratory items
- **AI-powered predictions**: Forecast item usage for any day, per item
- **Interactive web interface**: Built with Flask, modern UI, and charts
- **Command-line interface (CLI)**: For automation and scripting
- **Sample data and helper scripts**: For easy setup and learning
- **Unit tests**: For reliability and educational purposes

---

## Key Features

- **User Authentication**: Simple login system for demonstration
- **Items Table**: View all items, their categories, quantities, and predicted usage
- **AI Prediction**: Uses a machine learning model to predict item usage for any day, per item
- **Bar Chart Visualization**: See predicted usage for all items in a beautiful chart
- **Day Selector**: Instantly update predictions for any day
- **CLI Tools**: Login, predict, and train the model from the command line
- **Sample Data**: Preloaded for quick demo and testing
- **Helper Scripts**: For setup, development, and learning
- **Extensible**: Easy to add new features, data sources, or AI models

---

## Who Is This For?
- **Students**: Learn about databases, web development, AI, and software engineering
- **Educators**: Use as a teaching tool or assignment starter
- **Developers**: Extend for real-world laboratory management or research

---

## Technologies Used
- **Python 3.8+**
- **Flask** (web framework)
- **SQLite** (local database)
- **scikit-learn, pandas** (AI/ML)
- **Chart.js** (bar chart visualization)
- **HTML/CSS** (modern UI)

---

## How It Works
- **Database**: Stores users, items, and item usage (with sample/demo data)
- **AI Model**: Trained on usage data to predict future needs
- **Web App**: Login, view items, predict usage, and visualize data
- **CLI**: For automation, scripting, and testing
- **Helper Scripts**: For setup, development, and learning

---

## Getting Started
See the detailed instructions below for setup, running, and extending the project on Windows or Mac.

---

# laboratory_management


# Laboratory Management Project Structure:

```
laboratory_management/
│
├── app/
│   ├── config.py
│   ├── cli/
│   │   └── testcli.py
│   ├── db/
│   │   ├── database.py
│   │   └── insert_sample_data.py
│   ├── models/
│   │   └── models.py
│   ├── services/
│   │   ├── ai_item_model.py
│   │   └── test_google_service.py
│   └── utils/
│       └── user_validation.py
│
├── tests/
│   ├── test_ai_item_model.py
│   └── test_login.py
│
├── ui/
│   ├── static/
│   │   ├── items.css
│   │   ├── items_ui.css
│   │   └── login.css
│   └── templates/
│       ├── items_list.html
│       ├── items_ui.html
│       ├── login.html
│       └── predict.html
│       └── predict_bar.html
│
├── user_interface/
│   └── lab_management_app.py
│
├── requirements.txt
├── run.py
├── setup_helper.py
├── helper_dev.py
└── README.md
```

---

## How to Run This Application (Windows & Mac)

### 1. Clone the Repository
```
git clone <your-repo-url>
cd laboratory_management
```

### 2. Set Up Python Environment
- **Windows:**
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Requirements
```
pip install -r requirements.txt
```

### 4. Initialize the Database
```
python run.py
```

### 5. Insert Sample Data (for demo/testing)
```
python app/db/insert_sample_data.py
```

### 6. Train the AI Model (for item usage prediction)
```
python app/cli/testcli.py train-item-model
```

### 7. Run the Web Application
```
python user_interface/lab_management_app.py
```
- Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 8. Features
- **Login:** Use `admin` / `password123` for demo login.
- **Items Table:** View all items, their quantities, and predicted usage for a selected day.
- **Predict Usage:** Click the Predict Usage button to get item-specific predictions.
- **Show Usage Chart:** Click the Show Usage Chart button for a bar chart of all items' predicted usage.
- **Change Prediction Day:** Use the day selector at the top of the items or chart page to update predictions.

### 9. Command Line Interface (CLI)
- Login: `python app/cli/testcli.py login --username admin --password password123`
- Predict item usage: `python app/cli/testcli.py predict-item-usage --day 5`
- Train model: `python app/cli/testcli.py train-item-model`

### 10. Notes
- The app uses SQLite for local storage (file: `local_lab_management.db`).
- All sample data and models are for demonstration. Replace with your real data for production use.
- For any issues, ensure your Python version is 3.8+ and all dependencies are installed.

---

## Quick Setup (Recommended)

After cloning the repository, you can use the provided helper script to set up everything automatically:

```
python setup_helper.py
```

This script will:
- Create a virtual environment
- Install all requirements
- Initialize the database
- Insert sample data
- Train the AI model

After it finishes, follow the printed instructions to start the web app and open it in your browser.

If you are on Mac and `python` points to Python 2, use:
```
python3 setup_helper.py
```

---

## Developer Helper Script

For students and developers, a helper script is provided with common commands and tips:

```
python helper_dev.py
```

This will print:
- How to activate the virtual environment
- How to run the web app
- How to insert your own data
- How to retrain the AI model
- How to use CLI commands
- How to run tests
- How to reset the database

Edit `helper_dev.py` to add more tips for your team or class!

---

## File/Script Overview
- `run.py`: Initializes the database.
- `app/db/insert_sample_data.py`: Populates the database with sample items and usage data.
- `user_interface/lab_management_app.py`: Main Flask web app (login, items, prediction, chart).
- `app/cli/testcli.py`: Command-line interface for login and AI prediction.
- `app/services/ai_item_model.py`: AI model logic for item usage prediction.

---

## For Mac Users
- Use `python3` instead of `python` if needed.
- Use `source venv/bin/activate` to activate the virtual environment.

---

## For Developers
- Update `app/db/insert_sample_data.py` to add more items or usage data.
- Update `app/services/ai_item_model.py` for advanced AI/ML logic.
- UI templates are in `ui/templates/` and static files in `ui/static/`.

---

## How to Integrate Live Data in the Future

If you want to use live data (from sensors, APIs, or real-time user input) instead of sample/demo data, follow these steps:

1. **Update the Database Schema**
   - Add new columns or tables as needed (e.g., timestamps, sensor IDs).
   - Example: To add a timestamp to item usage:
     ```sql
     ALTER TABLE item_usage ADD COLUMN timestamp DATETIME;
     ```

2. **Update Data Ingestion Logic**
   - Replace or supplement `app/db/insert_sample_data.py` with code that fetches or receives live data.
   - Example: Write a script or API endpoint to insert new usage records as they arrive.

3. **Update AI Model Training**
   - Ensure your AI model uses the latest/live data for training and prediction.
   - Retrain the model periodically or after new data is added.

4. **Update the Web App**
   - Modify Flask routes to display live data.
   - For real-time updates, consider using AJAX or WebSockets in the UI.

5. **Remove or Archive Demo Data**
   - Once live data is flowing, you can remove or archive the sample/demo data logic.

**Developer Tips:**
- Replace the logic in `app/db/insert_sample_data.py` with your live data ingestion code.
- Update the `item_usage` table schema if your live data has new fields.
- Make sure your AI model in `app/services/ai_item_model.py` uses the new data format.
- Test the web app and CLI to ensure they work with live data.

If you have a specific live data source (API, file, sensor, etc.), update the ingestion logic accordingly. For help, ask for a code example for your data source!