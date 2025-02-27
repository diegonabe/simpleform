from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Cargar la configuración desde config.py
    app.config.from_object(Config)

    # Definir la clave secreta para Flask-WTF
    app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Puedes mover esto a config.py si prefieres

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Importar y registrar las rutas
    from app.routes import main
    app.register_blueprint(main)

    return app
