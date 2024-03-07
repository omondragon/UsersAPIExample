from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from users.models.db import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(user_controller)

# Ruta para renderizar el template index.html
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

