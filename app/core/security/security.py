# from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBearer
# Here, fastAPI extracts Bearer token from authorization header
# and passes token to dependency

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
oauth2_scheme = HTTPBearer()