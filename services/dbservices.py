from repository import db_controller

def getdata(query):
    return db_controller.executequery(query)