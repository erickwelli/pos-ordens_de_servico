from app.extensions import ma
from app.models.service_order import ServiceOrder
from marshmallow import fields, validate

class ServiceOrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ServiceOrder

    id = ma.auto_field(dump_only=True)

    descricao = ma.auto_field(required=True)

    status = fields.String(
        required=True,
        validate=validate.OneOf(
            ["aberta", "em andamento", "concluida"]
        )
    )

    service_id = ma.auto_field(required=True)

    service = fields.Nested(
        "ServiceSchema",
        only=("id", "nome")
    )