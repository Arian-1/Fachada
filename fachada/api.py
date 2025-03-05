from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

class ServicioA:
    def ejecutar(self):
        return "Servicio A ejecutado."

class ServicioB:
    def ejecutar(self):
        return "Servicio B ejecutado."

class Fachada:
    def __init__(self):
        self.servicio_a = ServicioA()
        self.servicio_b = ServicioB()

    def operacion_compleja(self):
        resultado_a = self.servicio_a.ejecutar()
        resultado_b = self.servicio_b.ejecutar()
        return f"{resultado_a} | {resultado_b}"

fachada = Fachada()

@app.route('/api/fachada', methods=['GET'])
def obtener_datos():
    """
    Endpoint para acceder a la fachada.
    ---
    responses:
      200:
        description: Datos procesados correctamente
    """
    mensaje = fachada.operacion_compleja()
    return jsonify({"mensaje": mensaje})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

