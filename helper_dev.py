"""
helper_dev.py

A collection of helper scripts and code snippets for students and developers to understand, test, and extend the laboratory management system.
"""
import os
import sys
import platform
import subprocess

# 1. How to activate the virtual environment

def print_activate_venv():
    if platform.system() == 'Windows':
        print('Activate venv: .\\venv\\Scripts\\activate')
    else:
        print('Activate venv: source venv/bin/activate')

# 2. How to run the web app

def print_run_web():
    print('Run the web app: python user_interface/lab_management_app.py')
    print('Then open http://127.0.0.1:5000/ in your browser.')

# 3. How to insert your own data

def print_insert_data():
    print('Edit app/db/insert_sample_data.py to add your own items and usage data.')
    print('Then run: python app/db/insert_sample_data.py')

# 4. How to retrain the AI model after adding new data

def print_train_model():
    print('Retrain AI model: python app/cli/testcli.py train-item-model')

# 5. How to run CLI commands

def print_cli_examples():
    print('Login: python app/cli/testcli.py login --username admin --password password123')
    print('Predict item usage: python app/cli/testcli.py predict-item-usage --day 5')

# 6. How to run tests

def print_run_tests():
    print('Run all tests: python -m unittest discover tests')

# 7. How to reset the database (for a clean start)
def print_reset_db():
    print('To reset the database, delete local_lab_management.db and rerun run.py and insert_sample_data.py')

if __name__ == "__main__":
    print("\n=== Developer Helper Script ===\n")
    print_activate_venv()
    print_run_web()
    print_insert_data()
    print_train_model()
    print_cli_examples()
    print_run_tests()
    print_reset_db()
    print("\n---\nEdit this file to add more helper tips for your team or students!\n")
