import mysql.connector

def dbconnect():
  mydb = mysql.connector.connect(host='145.89.192.95', user='dbuser', passwd='Dbuser123!', database='ontime')
  return mydb

def getpeople():
  people = []
  sql = 'SELECT * FROM people;'
  mydb = dbconnect()
  mycursor = mydb.cursor()
  mycursor.execute(sql)
  for (record) in mycursor:
    people.append(record)
  mycursor.close()
  mydb.close()
  return people



