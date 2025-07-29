import jwt
import timefrom
import Path

private_key = Path("path_to_private_key").read_text()

payload = {
    'iat': int(time.time()),
    'exp': int(time.time()),
    'iss': "1661220"
}

jwt_token = jwt.encode(payload, private_key, algorithm='RS256')
print("jwt token:", jwt_token)