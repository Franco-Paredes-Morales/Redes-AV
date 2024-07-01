from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/prueba', methods=['GET'])
def prueba():
    resultado = tu_funcion_principal()
    return jsonify({"resultado": resultado})

def tu_funcion_principal():
    # Aquí pones la lógica de tu código
    return "Hola, este es un script de prueba para redes."

if __name__ == "__main__":
    app.run(debug=True)
