from app.extensions import db
from app.models.service import Service
from app.models.service_order import ServiceOrder
from app.schemas.service_order_schema import ServiceOrderSchema
from app.utils.response import success_response

order_schema = ServiceOrderSchema()
orders_schema = ServiceOrderSchema(many=True)


def listar_ordens():
    ordens = ServiceOrder.query.all()
    return success_response(orders_schema.dump(ordens))


def listar_ordens_por_servico(service_id):
    servico = Service.query.get_or_404(service_id)

    return success_response(
        orders_schema.dump(servico.orders)
    )


def criar_ordem(data):
    dados_validados = order_schema.load(data)

    Service.query.get_or_404(
        dados_validados["service_id"]
    )

    nova_ordem = ServiceOrder(**dados_validados)

    db.session.add(nova_ordem)
    db.session.commit()

    return success_response(
        order_schema.dump(nova_ordem),
        201
    )


def atualizar_status_ordem(id, data):
    ordem = ServiceOrder.query.get_or_404(id)

    dados_validados = order_schema.load(
        data,
        partial=True
    )

    if "status" in dados_validados:
        ordem.status = dados_validados["status"]

    db.session.commit()

    return success_response(
        order_schema.dump(ordem)
    )