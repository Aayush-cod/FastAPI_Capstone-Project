from datetime import datetime, timezone , timedelta
from jose import jwt , JWTError
from app.core.config import settings

def create_token(data: dict, expiry_minutes = 30):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes = expiry_minutes)

    to_encode.update({'exp': expiry})
    return jwt.encode(to_encode , settings.JWT_SECRET_KEY , algorithm = settings.JWT_ALGORTIHM)


def verify_token(token : str):
    try:
        payload = jwt.decode(token , settings.JWT_SECRET_KEY, algorithms = [settings.JWT_ALGORTIHM])
        return payload
    except JWTError:
        pass    