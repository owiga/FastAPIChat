import sqlite3

class ChatDatabase:
    def __init__(self):
        self.db_name = "db/chat.db"
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS messages
                       (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           text TEXT
                       )
                       """)
        conn.commit()

    def add_message(self, text: str):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (text) VALUES (?)", (text,))
        conn.commit()
        conn.close()

    def get_history(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM messages ORDER BY id DESC LIMIT 50")
        rows = cursor.fetchall()
        conn.close()
        return rows

database = ChatDatabase()