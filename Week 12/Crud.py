import sqlite3

def connect():
    return sqlite3.connect("app.db")

def create_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def add_user(name, age):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()

def view_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()
    return data


# RUN CODE
if __name__ == "__main__":
    create_database()
    add_user("Ali", 23)
    print(view_users())