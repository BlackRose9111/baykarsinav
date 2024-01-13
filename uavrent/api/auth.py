from datetime import datetime, timedelta
import jwt

SECRET_KEY = "AAAAB3NzaC1yc2EAAAADAQABAAABAQC7LaXlSnyXnvFojpzKMYftub/Lx52klZS/T0ktaEx3nczwg19G/DLqs2zFHQHxuBglNsOopJOhZvMWm+XxGAW/jZLF2etwHr4tXVAMrkZNeU1pCZg++tIJ6j724SVbWu8G1A59NnDhNgBsaRFNVTtCoKrQnRb940HqgkxvQqx1xt7T4kmFgNbsH/mcDuKzEND6fQLJ1mqFjLnCwJRBUp9yXJRjch1PFullE7ST+qJhgcosYW+J0fUHAaYeXkpCyAwsVtQEDx9p0Za/SfIf1dm7RC5zB"
def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

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

#the reason I implemented my own JWT based authentication instead of the default one
#is because I could not truly understand how the default authentication would work(or if it would work at all) with
#the rest API. I still used the default authentication method to compare password and usernaem
#because it was already there to be used, probably not the best practice.
#JWT is a token based authentication method, it is stateless and does not require a database to store tokens
#I figured it was a better option for APIs, APIs can have sessionless API keys and this is a similar concept
#REST API does allow us to turn a portion of our project into third party accessible APIs
#As well as allowing a fully backend only project with no frontend