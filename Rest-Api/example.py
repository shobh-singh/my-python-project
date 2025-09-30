from flask import Flask,jsonify

app=Flask(__name__)


student=[
    {"id":3,"name":'vikram',"age":90}
]

@app.route('/students',methods=["Get"])
def fun():
    return jsonify(student),200

@app.route('/')
def fun1():
    return 'Hello, world'

if __name__=="__main__":
    app.run(debug=True)