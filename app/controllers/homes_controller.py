from app import app
from flask import (
    Flask,
    request,
    make_response,
)
from app.models.home import Home
from app.middleware.auth import token_required

# ==============================set product dan lainnya di sini=========================
# contoh untuk mencari produk sebelum dihapus
# ==============================end set product dan lainnya di sini=========================


# ==============================routing=========================
@app.route(
    "/home", methods=["GET"]
)  # routing all_home, show_home, update_home, create_home, destroy_home
@token_required  # authentication
def all_home(a, b):
    print(a, b)
    data = Home.get_data("a", "b")
    return make_response(
        {"msg": "Data kolam nda ada", "status": 200, "data": data}, 200
    )
