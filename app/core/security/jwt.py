from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "Purgatory"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRES_MINUTES = 60

# TEST ON JWT.IO
ACCESS_TOKEN_EXPIRES_MINUTES = 2

def create_access_token(data:dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRES_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode, SECRET_KEY, algorithm = ALGORITHM
    )

def decode_access_token(token:str):
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None