import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import argparse
from app.utils.user_validation import validate_user_login


def main():
    parser = argparse.ArgumentParser(description="Laboratory Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Login command
    login_parser = subparsers.add_parser("login", help="User login")
    login_parser.add_argument("--username", required=True, help="Username")
    login_parser.add_argument("--password", required=True, help="Password")

    # AI model commands
    ai_parser = subparsers.add_parser("predict-item-usage", help="Predict item usage for a given day")
    ai_parser.add_argument("--day", type=int, required=True, help="Day number for prediction")

    # AI model train command
    train_parser = subparsers.add_parser("train-item-model", help="Train AI item usage model from DB")

    args = parser.parse_args()

    if args.command == "login":
        if validate_user_login(args.username, args.password):
            print("Login successful!")
        else:
            print("Invalid username or password.")
    elif args.command == "predict-item-usage":
        from app.services.ai_item_model import predict_item_usage
        prediction = predict_item_usage(args.day)
        print(f"Predicted item usage for day {args.day}: {prediction:.2f}")
    elif args.command == "train-item-model":
        from app.services.ai_item_model import train_model_from_db
        try:
            train_model_from_db()
            print("AI item usage model trained from database.")
        except Exception as e:
            print(f"Training failed: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
