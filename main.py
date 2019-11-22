from flask import Flask, escape, request, jsonify
import os
app = Flask(__name__)

dictTasks = {}
global tasksId
tasksId = 0

class Tasks:
    def __init__(self,name ,description):
        
        self.name = name
        self.description = description

# Atribui ao dicionario primeiro elemento as tasks
dictTasks[tasksId] = Tasks(1,2)
tasksId =+ 1

@app.route('/Tarefa/',methods=['GET'])
def getTasks():
    resp = [[i.name, i.description] for i in dictTasks.values()]
    return jsonify(resp)

@app.route('/Tarefa/',methods=['POST'])
def postTasks():
    global tasksId
    dictTasks[tasksId] = Tasks(request.form.get('name'),request.form.get('description'))
    tasksId =+ 1
    return "OK"

@app.route('/Tarefa/<id>',methods=['GET'])
def getTasksID(id):
    id = int(id)
    resp = (dictTasks[id].name, dictTasks[id].description)
    print(dictTasks.keys())
    return jsonify(resp)

@app.route('/Tarefa/<id>', methods = ['PUT'])
def updateTask(id):
    id = int(id)
    dictTasks[id].name = request.form.get('name')
    dictTasks[id].description = request.form.get('description')
    return "OK"

@app.route('/Tarefa/<id>', methods = ['DELETE'])
def deleteTask(id):
    id = int(id)
    del dictTasks[id]
    return "OK"
@app.route('/healthcheck/', methods = ['GET'])
def healthTask():
    return "",200











