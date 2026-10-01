from flask import Flask, jsonify, request

app = Flask(__name__)

datos = [{'id': 1, 'documento': '1001001', 'nombre': 'Laura Pérez', 'edad': 29}, {'id': 2, 'documento': '1001002', 'nombre': 'Carlos Martínez', 'edad': 45}, {'id': 3, 'documento': '1001003', 'nombre': 'Ana Gómez', 'edad': 36}]

@app.get("/")
def inicio():
    return jsonify({
        "servicio": "Pacientes",
        "estado": "activo",
        "recurso": "/pacientes"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/pacientes")
def listar():
    return jsonify(datos), 200

@app.get("/pacientes/<int:item_id>")
def obtener(item_id):
    item = next((x for x in datos if x["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Registro no encontrado"}), 404
    return jsonify(item), 200

@app.post("/pacientes")
def crear():
    nuevo = request.get_json(silent=True)
    if not isinstance(nuevo, dict):
        return jsonify({"error": "Se requiere un cuerpo JSON válido"}), 400

    nuevo["id"] = max([x["id"] for x in datos], default=0) + 1
    datos.append(nuevo)
    return jsonify(nuevo), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
