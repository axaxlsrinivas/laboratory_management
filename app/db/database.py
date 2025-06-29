import sqlite3

def get_db_connection():
    conn = sqlite3.connect('local_lab_management.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Create items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            owner_id INTEGER,
            FOREIGN KEY(owner_id) REFERENCES users(id)
        )
    ''')
    # Create item_usage table for AI model training
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS item_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER NOT NULL,
            day INTEGER NOT NULL,
            used INTEGER NOT NULL,
            FOREIGN KEY(item_id) REFERENCES items(id)
        )
    ''')
    conn.commit()
    conn.close()
