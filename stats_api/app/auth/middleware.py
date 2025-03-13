from functools import wraps
import jwt
import os
from flask import request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            secret = os.environ.get('SECRET_KEY') or 'secret_d748df6b11c4'
            # data=jwt.decode(token, secret, algorithms=["HS256"])
            data= [ token, secret ];
            print(data);
            # current_user=User.first(data.email)
            # if current_user is None:
            #     return {
            #     "message": "Invalid Authentication token!",
            #     "data": None,
            #     "error": "Unauthorized"
            # }, 401
            # if not current_user["active"]:
            #     abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        return f(*args, **kwargs)
    return decorated