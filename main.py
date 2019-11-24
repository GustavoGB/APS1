from flask import Flask, escape, request, jsonify
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["teste"]
col = db["banas"]

class Tasks:
    def __init__(self,name ,description):
        
        self.name = name
        self.description = description

@app.route('/Tarefa/',methods=['GET'])
def getTasks():
    resp = [[i['name'],i['description']] for i in list(col.find({}))]
    return jsonify(resp)

@app.route('/Tarefa/',methods=['POST'])
def postTasks():
    col.insert_one({"name":request.form.get('name'),"description":request.form.get('description')})
    return "OK"

@app.route('/Tarefa/<name>',methods=['GET'])
def getTasksID(name):
    resp = [[i.name, i.description] for i in list(db.collection.find({"name":name}))]
    return jsonify(resp)

@app.route('/Tarefa/<name>', methods = ['PUT'])
def updateTask(name):
    col.update_one({'name': name}, {"$set":{"name":request.form.get('name'),"description":request.form.get('description')}})
    return "OK" 

@app.route('/Tarefa/<name>', methods = ['DELETE'])
def deleteTask(name):
    col.delete_one({"name": name})
    return "OK"

@app.route('/healthcheck/', methods = ['GET'])
def healthTask():
    return "",200

if __name__ == '__main__':
    app.run()