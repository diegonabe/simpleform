# Simple Form Project

Este es un proyecto de formulario en Flask que guarda datos en una base de datos PostgreSQL.

## 🚀 Requisitos

- Python 3.12+
- PostgreSQL
- Virtualenv
- Git

## 📦 Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd simple_form_project
   ```

2. Crea un entorno virtual e instálalo:

   ```sh
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\\Scripts\\activate  # Windows
   pip install -r requirements.txt
   ```

3. Configura la base de datos en `config.py` y crea las tablas:

   ```sh
   flask db init
   flask db migrate -m "Inicialización de la base de datos"
   flask db upgrade
   ```

## ▶️ Ejecución

Para correr el servidor Flask:

```sh
flask run
```

Accede a `http://127.0.0.1:5000` en tu navegador.