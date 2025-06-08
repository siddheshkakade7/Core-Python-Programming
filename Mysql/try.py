# Mysql connector
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "newdb"
)
# Creating database
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabse")


# # SHOW DATABASES
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)


# Creating a table :
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")

# Alter Table :
# mycursor.execute("ALTER TABLE customers ADD COLUMN Email VARCHAR(255)")

# mydb.commit()

# Insert a single record :

# sql= "INSERT INTO customers (name,address,Email) VALUES(%s,%s,%s)"
# val=('Siddhesh','Pune',"kakadesiddhesh777@gmail.com")
# mycursor.execute(sql,val)

# Inserting Multiple records :
# sql= "INSERT INTO customers (name,address,Email) VALUES(%s,%s,%s)"
# Val = [('abc','def','abc@fgmail.com'),('abcd','defd','abcd@fgmail.com')]
# mycursor.executemany(sql,Val)
# mydb.commit()

# To select only some of the columns in a table

# mycursor.execute("SELECT name,address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# WHERE
# mycursor.execute("SELECT *FROM customers WHERE address='Pune'")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# DELETE FROM statement :
# mycursor.execute("DELETE FROM customers WHERE name = 'Siddhesh'")

# mydb.commit()     # it is required to make changes

# DROP TABLE statement :
# mycursor.execute("CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")
# mycursor.execute("DROP TABLE customer")

# Update
# mycursor.execute("UPDATE customers SET address = 'Canyon 123' WHERE address = 'Pune'")

# mydb.commit()