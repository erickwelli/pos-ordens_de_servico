from flask import Flask

from .config import Config
from .extensions import db, migrate, ma, jwt

from .routes.services import services_bp
from .routes.orders import orders_bp
from .routes.users import users_bp
from .routes.auth import auth_bp

from marshmallow import ValidationError
from werkzeug.exceptions import NotFound



def create_app():

    app = Flask(__name__)


    app.config.from_object(Config)


    db.init_app(app)

    migrate.init_app(
        app,
        db
    )

    ma.init_app(app)

    jwt.init_app(app)



    # Importa os models para o SQLAlchemy reconhecer
    from .models import User, Service, ServiceOrder



    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(orders_bp, url_prefix="/orders")

    app.register_blueprint(
        users_bp,
        url_prefix="/users"
    )

    app.register_blueprint(
        auth_bp
    )



    @app.errorhandler(ValidationError)
    def handle_validation_error(err):

        return {
            "success": False,
            "errors": err.messages
        }, 400



    @app.errorhandler(NotFound)
    def handle_not_found(err):

        return {
            "success": False,
            "message": "Recurso não encontrado"
        }, 404



    @app.errorhandler(404)
    def handle_404(err):

        return {
            "success": False,
            "message": "Rota não encontrada"
        }, 404



    return app