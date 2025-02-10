import mysql.connector

    # Establish a connection to the MySQL database
mydb = mysql.connector.connect(
        host='localhost',  # Make sure your MySQL server is running locally
        user='root',       # Replace with the correct username
        password='Ajay123@',  # Replace with the correct password
        database='college'   # Specify the database name if needed
    )
mycursor = mydb.cursor()
 


sql="insert into stud(name, city, age, rollno) , values(%s,%s,%s,%s)"
val = ("ajay", "indore", 45, "22hsgwj"),


mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")

