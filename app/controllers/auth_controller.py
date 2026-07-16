from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.models.user import User

def login_usuario(data):

    email = data.get("email")

    senha = data.get("senha")


    usuario = User.query.filter_by(
        email=email
    ).first()


    if not usuario:
        return {
            "success": False,
            "message": "Email ou senha inválidos"
        }, 401



    senha_valida = check_password_hash(
        usuario.senha,
        senha
    )


    if not senha_valida:

        return {
            "success": False,
            "message": "Email ou senha inválidos"
        }, 401



    token = create_access_token(
        identity=str(usuario.id)
    )


    return {
        "success": True,
        "access_token": token
    }, 200