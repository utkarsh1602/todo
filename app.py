from flask import Flask, Response, jsonify, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

from werkzeug.wrappers import response

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#DATABASE
class Todo(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500))
    created = db.Column(db.DateTime, default = datetime.now())

    # def __repr__(self) -> str:
    #     return f'{self.title} - {self.created}'

@app.route("/todo_create", methods=["GET","POST"])
def create_todo():
    
    if request.method=="POST":
        data = json.loads(request.data)
        title = data.get("title")
        desc = data.get("desc")
        if all([title, desc]):
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
            response = {"status":201, "msg": "Todo created", "payload":data}
            return jsonify(response)
        else:
            response = {"status":200, "msg": "Incomplete data", "payload":data}
            return jsonify(response)    
    
    return Response("No data posted")
    
@app.route("/todo_all")    
def read_todo_all():
    todos = Todo.query.all()
    data = list(map(lambda x: {
        "id" : x.s_no,
        "Title" : x.title,
        "Description" : x.desc,
        "Created On" : x.created
    }, todos))
    response = {"status":200, "payload":data}
    return jsonify(response)

@app.route("/todo_get") 
def read_todo():
    if request.method=="GET":
        data = json.loads(request.data)
        id = data.get("s_no")
        todo = Todo.query.get(ident=id)
        data = todo.title
        response = {"status":200, "payload":data}
        return jsonify(response)

@app.route("/todo_update", methods=["PUT"])
def update_todo():
    data = json.loads(request.data) 
    id = data.get("s_no")
    todo = Todo.query.get(ident=id)
    todo = {
        "id" : todo.s_no,
        "Title" : todo.title,
        "Description" : todo.desc,
        "Created On" : todo.created
    }
    db.session.add(todo)
    db.session.commit()
    return jsonify({})       

if __name__ == "__main__":
    app.run(debug=True)    

