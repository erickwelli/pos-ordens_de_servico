from flask import Blueprint, jsonify, request

from app.controllers.auth_controller import login_usuario



auth_bp = Blueprint(
    "auth",
    __name__
)



@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()


    response, status = login_usuario(
        data
    )


    return jsonify(response), status