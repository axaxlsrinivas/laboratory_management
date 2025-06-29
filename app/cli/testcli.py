import argparse
from app.utils.user_validation import validate_user_login


def main():
    parser = argparse.ArgumentParser(description="Laboratory Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Login command
    login_parser = subparsers.add_parser("login", help="User login")
    login_parser.add_argument("--username", required=True, help="Username")
    login_parser.add_argument("--password", required=True, help="Password")

    args = parser.parse_args()

    if args.command == "login":
        if validate_user_login(args.username, args.password):
            print("Login successful!")
        else:
            print("Invalid username or password.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
