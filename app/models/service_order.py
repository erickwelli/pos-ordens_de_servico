from app.extensions import db

class ServiceOrder(db.Model):
    __tablename__ = "service_orders"

    id = db.Column(db.Integer, primary_key=True)

    descricao = db.Column(db.String(255), nullable=False)

    status = db.Column(db.String(50), nullable=False)

    service_id = db.Column(
        db.Integer,
        db.ForeignKey("services.id"),
        nullable=False
    )