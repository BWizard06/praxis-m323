from flask import Flask, jsonify, request
from functools import reduce

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

#B2G & B2F
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def perform_operation(func, x, y):
    return func(x, y)

@app.route('/calculate/<operation>/<int:x>/<int:y>', methods=['GET'])
def calculator_endpoint(operation, x, y):
    operations = {
        "add": add,
        "subtract": subtract
    }

    if operation in operations:
        result = perform_operation(operations[operation], x, y)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Operation not supported"}), 400
    
#B2E
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

@app.route('/closure/<int:x>/<int:y>', methods=['GET'])
def closure_endpoint(x, y):
    func = outer_function(x)
    result = func(y)
    return jsonify({"result": result})

#B3G
@app.route('/square/<int:n>', methods=['GET'])
def square_number(n):
    square = lambda x: x * x
    return jsonify({"result": square(n)})

@app.route('/uppercase/<string:text>', methods=['GET'])
def uppercase_text(text):
    to_upper = lambda s: s.upper()
    return jsonify({"result": to_upper(text)})

#B3F
@app.route('/lambda_multiply', methods=['POST'])
def lambda_multiply_endpoint():
    data = request.get_json()
    multiply = lambda x, y: x * y
    result = multiply(data['x'], data['y'])
    return jsonify({"result": result})

#B3E
@app.route('/sort_students', methods=['POST'])
def sort_students_endpoint():
    data = request.get_json()
    students = data['students']
    # Sortiert die Schülerliste basierend auf den Noten mit einem Lambda-Ausdruck
    sorted_students = sorted(students, key=lambda x: x['grade'])
    return jsonify({"sorted_students": sorted_students})


#B4G
@app.route('/apply_functions', methods=['POST'])
def apply_functions():
    data = request.json
    numbers = data['numbers']
    mapped = list(map(lambda x: x * 2, numbers))
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    reduced = reduce(lambda x, y: x + y, numbers)
    return jsonify({"mapped": mapped, "filtered": filtered, "reduced": reduced})

#B4F
@app.route('/combine_functions', methods=['POST'])
def combine_functions():
    data = request.json
    numbers = data['numbers']
    result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))
    return jsonify({"result": result})

#B4E
@app.route('/complex_data_processing', methods=['POST'])
def complex_data_processing():
    data = request.json
    users = data['users']
    
    # Extrahiere Gehälter, filtere Nutzer mit Gehalt > 5000 und berechne Durchschnitt
    average_salary = reduce(lambda x, y: x + y, filter(lambda salary: salary > 5000, map(lambda user: user['salary'], users))) / len(users)
    
    return jsonify({"average_salary": average_salary})

if __name__ == '__main__':
    app.run()