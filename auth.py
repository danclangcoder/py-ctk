from pass_utils import create_password, verify_password
from database import add_user, get_user, update_username, update_password
from sqlite3 import IntegrityError


def register(username, password) -> tuple[bool, str]:
    if not username or not password:
        return False, "Username and password required."

    password = create_password(password)

    try:
        add_user(username, password)
        return True, "User registered successfully."
    except IntegrityError:
        return False, "Username already exists."


def login(username, password) -> tuple[bool, str]:
    result = get_user(username)

    if result is None:
        return False, "User not found."

    stored_password = result[1]

    if verify_password(stored_password, password):
        return True, "Login successful."
    else:
        return False, "Invalid credentials."
    
def change_username(your_uname, new_uname):
    update_username(your_uname, new_uname)
    username, _ = get_user(new_uname)
    print(f'{your_uname} changed to {username}')

def change_password(your_uname, new_pass):
    user_old, pass_old = get_user(your_uname)
    your_pass = create_password(new_pass)
    update_password(your_uname, your_pass)