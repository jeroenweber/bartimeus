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

def getpeople():
  global mycursor
  people = []
  sql = 'SELECT * FROM people;'
  mycursor.execute(sql)
  for (record) in mycursor:
    people.append(record)
  return people

def executequery(query):
  dbconnect()
  if (query == 'people'):
    resultset = getpeople()
  else:
    resultset = ''
  dbclose()
  return resultset