from functools import wraps
from flask import request, abort
from flask import (
    Flask,
    request,
    make_response,
    jsonify,
    render_template,
    redirect,
    url_for,
)

def token_required(f):
    def decorator(*args, **kwargs):
        # token = request.args.get("token")

        # if False:
        #     return make_response(jsonify({"msg": "tokennya nggak ada bro"}), 404)

        try:
            a = 2
            b = 3
            # output = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            # set current user
        except:
            return make_response(jsonify({"msg": "token nggak bener / invalid"}))
        return f(a, b)

    return decorator
