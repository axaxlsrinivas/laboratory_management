import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app.db.database import get_db_connection

def insert_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Insert sample items if not exist
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description, owner_id) VALUES (1, 'Beaker', 'Glassware item', NULL)")
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description, owner_id) VALUES (2, 'Test Tube', 'Glassware item', NULL)")
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description, owner_id) VALUES (3, 'Microscope', 'Equipment item', NULL)")
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description, owner_id) VALUES (4, 'Bunsen Burner', 'Equipment item', NULL)")
    # Insert sample usage data for all items
    usage_data = [
        (1, 1, 10), (1, 2, 12), (1, 3, 13), (1, 4, 15), (1, 5, 16),
        (2, 1, 20), (2, 2, 22), (2, 3, 21), (2, 4, 23), (2, 5, 25),
        (3, 1, 2), (3, 2, 2), (3, 3, 3), (3, 4, 4), (3, 5, 5),
        (4, 1, 5), (4, 2, 6), (4, 3, 7), (4, 4, 8), (4, 5, 9)
    ]
    for item_id, day, used in usage_data:
        cursor.execute("INSERT INTO item_usage (item_id, day, used) VALUES (?, ?, ?)", (item_id, day, used))
    conn.commit()
    conn.close()
    print("Sample data inserted.")

if __name__ == "__main__":
    insert_sample_data()
