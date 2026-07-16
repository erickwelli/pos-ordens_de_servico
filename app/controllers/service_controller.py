from app.extensions import db
from app.models.service import Service
from app.schemas.service_schema import ServiceSchema
from app.utils.response import success_response

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


def listar_servicos():
    servicos = Service.query.all()
    return success_response(services_schema.dump(servicos))


def criar_servico(data):
    dados_validados = service_schema.load(data)

    novo_servico = Service(**dados_validados)

    db.session.add(novo_servico)
    db.session.commit()

    return success_response(service_schema.dump(novo_servico), 201)