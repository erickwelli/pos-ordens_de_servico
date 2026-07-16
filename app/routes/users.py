from flask import Blueprint, jsonify, request

from app.controllers.user_controller import criar_usuario


users_bp = Blueprint(
    "users",
    __name__
)



@users_bp.route("/", methods=["POST"])
def post_user():

    data = request.get_json()


    response, status = criar_usuario(
        data
    )


    return jsonify(response), status