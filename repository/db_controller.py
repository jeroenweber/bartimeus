import mysql.connector

global mydb
global mycursor

def dbconnect():
  global mydb, mycursor
  mydb = mysql.connector.connect(host='145.89.192.95', user='dbuser', passwd='Dbuser123!', database='ontime')
  mycursor = mydb.cursor(prepared=True)

def dbclose():
  global mydb, mycursor
  mycursor.close()
  mydb.close()

def dbcommit():
  global mydb
  mydb.commit()

def nextid(query):
  resultset = executequery(query)
  maxid = resultset[0][0]
  resultset = resultset[1:]
  for record in resultset:
    if (record[0] > maxid):
      maxid = record[0]
  return (maxid+1)

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
  return resultset

def insert(record):
  global mycursor
  dbconnect()
  sql = """ INSERT INTO people VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  idplusone = nextid('people')
  # tuple to insert at placeholder
  tuple1 = (idplusone,record[0],record[1], record[2],record[3],record[4],record[5],record[6],record[7],record[8])
  mycursor.execute(sql, tuple1)
  dbcommit()
  dbclose()
  return("Data inserted successfully into employee table using the prepared statement")

def delete(id):
  global mycursor
  dbconnect()
  sql_Delete_query = """Delete from people where id = %s"""
  mycursor.execute(sql_Delete_query, (id,))
  dbcommit()
  dbclose()
  print("Record Deleted successfully using Parameterized query")
