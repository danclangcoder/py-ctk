from sqlite3 import connect


def get_connection():
    return connect('app.db')

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            '''
        )
        conn.commit()

def add_user(u, p):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (u, p,)
        )
        conn.commit()

def get_user(u):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT username, password FROM users WHERE username = ?',
            (u,)
        )
        return cursor.fetchone()
    
def update_username(old_u, new_u):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE users SET username = (?) WHERE username = (?)',
            (new_u,old_u,)
        )
        conn.commit()

def update_password(u, new_pass):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE users SET password = (?) WHERE username = (?)',
            (new_pass, u,)
        )
        conn.commit()

def delete_table(table_name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        conn.commit()

def remove_user(u):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM users WHERE username = ?',
            (u,)
        )
        conn.commit()

init_db()
