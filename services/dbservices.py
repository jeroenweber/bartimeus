from repository import db_controller

def getdata(query):
    return db_controller.executequery(query)

def insertdata(data):
    resultset = []
    for record in data:
        result = db_controller.insert(record)
        resultset.append(result)
    return resultset

def deleterecord(id):
    print('id =' + id)
    result = ''
    #result = db_controller.delete(id)
    return result
