from flask import Flask, jsonify;

app = Flask(__name__)

students = [
    {"id":1, "name":'vikram', "age":19},
    {"id":2, "name":'prakash', "age":20}
]

@app.route('/student',methods=["Get"])
def hello():
    return jsonify(students),200
if __name__=="__main__":
    app.run(debug=True)
