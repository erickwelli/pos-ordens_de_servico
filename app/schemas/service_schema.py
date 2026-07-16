from app.extensions import ma
from app.models.service import Service
from marshmallow import fields

class ServiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Service

    id = ma.auto_field(dump_only=True)

    nome = ma.auto_field(required=True)

    descricao = ma.auto_field(required=True)

    preco_base = ma.auto_field(required=True)

    orders = fields.Nested(
        "ServiceOrderSchema",
        many=True,
        dump_only=True,
        exclude=("service",)
    )