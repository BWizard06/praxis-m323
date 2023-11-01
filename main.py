from flask import Flask, jsonify

app = Flask(__name__)

#A1G
# Reine Funktion
def addieren(a, b):
    return a + b

@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add_route(a, b):
    result = addieren(a, b)
    return jsonify({"Ergebnis": result})

#A1F
@app.route('/immutable')
def immutable_values():
    tupel = (1, 2, 3)
    # Hier versuchen wir, den Wert in einem Tupel zu ändern, was nicht erlaubt ist,
    # da Tupel in Python unveränderlich sind.
    try:
        tupel[0] = 4
        message = "Wert wurde geändert."
    except TypeError:
        message = "Unveränderliche Werte können nicht geändert werden."
    
    return jsonify({"message": message})

#A1E
# OO-Ansatz
class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

# Prozeduraler Ansatz
def add_numbers(a, b):
    return a + b

# Funktionaler Ansatz
multiply = lambda x, y: x * y

@app.route('/compare')
def compare_methods():
    dog = Animal("Dog")
    sum_result = add_numbers(5, 3)
    multiply_result = multiply(5, 3)
    
    return jsonify({
        "OO_Result": dog.get_species(),
        "Procedural_Result": sum_result,
        "Functional_Result": multiply_result
    })

if __name__ == '__main__':
    app.run()