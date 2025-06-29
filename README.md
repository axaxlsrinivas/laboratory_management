# laboratory_management


# Laboratory Management_Project Structure:
library_management/
│
├── app/                           # Main application package
│   ├── __init__.py
│   ├── models/                    # Data models (e.g., Book, Member, Loan)
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── member.py
│   │   └── loan.py
│   │
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   ├── member_service.py
│   │   └── loan_service.py
│   │
│   ├── db/                        # Database interface
│   │   ├── __init__.py
│   │   ├── db.py                  # Connection / CRUD logic
│   │   └── seed_data.py
│   │
│   ├── cli/                       # Command Line Interface
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── utils/                     # Utility/helper functions
│   │   ├── __init__.py
│   │   └── validators.py
│   │
│   └── config.py                  # Configuration settings
│
├── tests/                         # Unit tests
│   ├── __init__.py
│   ├── test_books.py
│   ├── test_members.py
│   └── test_loans.py
│
├── requirements.txt              # List of required packages
├── README.md                     # Project overview
└── run.py                        # Entry point to launch the app

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
python user_interface/web_login.py
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
- `user_interface/web_login.py`: Main Flask web app (login, items, prediction, chart).
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