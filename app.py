from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola! La aplicación funciona en el puerto 5050."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
