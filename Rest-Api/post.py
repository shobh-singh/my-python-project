from flask import Flask, request, jsonify

app = Flask(__name__)
students = [2]

@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added successfull", "student": data}), 201



if __name__ == "__main__":
    app.run(debug=True)
