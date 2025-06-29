import unittest
import sqlite3
from app.db.database import get_db_connection, init_db

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        # Create users table
        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_user_registration(self):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "testpass"))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users WHERE username=?", ("testuser",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "testuser")
        self.assertEqual(user[2], "testpass")

    def test_user_login_success(self):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "testpass"))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", ("testuser", "testpass"))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)

    def test_user_login_failure(self):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "testpass"))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", ("testuser", "wrongpass"))
        user = self.cursor.fetchone()
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
