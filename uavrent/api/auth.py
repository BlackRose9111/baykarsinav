from datetime import datetime, timedelta
import jwt

SECRET_KEY = "AAAAB3NzaC1yc2EAAAADAQABAAABAQC7LaXlSnyXnvFojpzKMYftub/Lx52klZS/T0ktaEx3nczwg19G/DLqs2zFHQHxuBglNsOopJOhZvMWm+XxGAW/jZLF2etwHr4tXVAMrkZNeU1pCZg++tIJ6j724SVbWu8G1A59NnDhNgBsaRFNVTtCoKrQnRb940HqgkxvQqx1xt7T4kmFgNbsH/mcDuKzEND6fQLJ1mqFjLnCwJRBUp9yXJRjch1PFullE7ST+qJhgcosYW+J0fUHAaYeXkpCyAwsVtQEDx9p0Za/SfIf1dm7RC5zB"
def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')

def extract_user(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def is_jwt_valid(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False