from flask import Flask, jsonify, request

app = Flask(__name__)

#A1G
# Reine Funktion
def addieren(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

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

#B1G
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

@app.route('/bubble_sort', methods=['POST'])
def bubble_sort_endpoint():
    data = request.json['data']
    sorted_data = bubble_sort(data)
    return jsonify(sorted_data=sorted_data)

#B1F
@app.route('/berechne', methods=['POST'])
def berechne_endpoint():
    data = request.json
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation == "addieren":
        result = addieren(a, b)
    elif operation == "subtrahieren":
        result = subtraktion(a, b)
    else:
        return jsonify({"message": "Ungültige Operation"}), 400

    return jsonify({"result": result})

#B1E
def fibonacci(n):
    """Berechnet den n-ten Wert der Fibonacci-Folge."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci', methods=['POST'])
def fibonacci_endpoint():
    data = request.json
    num = data['num']
    result = fibonacci(num)
    return jsonify({"Ergebnis": result}), 200

if __name__ == '__main__':
    app.run()