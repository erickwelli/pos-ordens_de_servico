from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.utils.response import success_response
from werkzeug.security import generate_password_hash

user_schema = UserSchema()

users_schema = UserSchema(
    many=True
)



def criar_usuario(data):

    dados_validados = user_schema.load(data)


    senha_original = dados_validados["senha"]


    senha_criptografada = generate_password_hash(
        senha_original
    )


    novo_usuario = User(
        nome=dados_validados["nome"],
        email=dados_validados["email"],
        senha=senha_criptografada
    )


    db.session.add(
        novo_usuario
    )

    db.session.commit()


    return success_response(
        user_schema.dump(novo_usuario),
        201
    )