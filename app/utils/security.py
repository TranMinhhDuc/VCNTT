import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(10);
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
    
    