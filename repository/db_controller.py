import mysql.connector

global mydb
global mycursor

def dbconnect():
  global mydb, mycursor
  mydb = mysql.connector.connect(host='145.89.192.95', user='dbuser', passwd='Dbuser123!', database='ontime')
  mycursor = mydb.cursor()

def dbclose():
  global mydb, mycursor
  mycursor.close()
  mydb.close()

def executequery(query):
  global mycursor
  dbconnect()
  resultset = []
  if (query == 'people'):
    sql = 'SELECT * FROM people;'
  else:
    query = 'can be extended but never reached, use elif'
  mycursor.execute(sql)
  for (record) in mycursor:
    resultset.append(record)
  dbclose()
  return resultset