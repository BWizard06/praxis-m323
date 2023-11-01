from flask import Flask, jsonify

app = Flask(__name__)

# Reine Funktion
def addieren(a, b):
    return a + b

@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add_route(a, b):
    result = addieren(a, b)
    return jsonify({"Ergebnis": result})

if __name__ == '__main__':
    app.run()