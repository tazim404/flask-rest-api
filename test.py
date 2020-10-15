import requests
import sqlite3
name=input("Enter your name:-\t")
age=input("Enter your age:-\t")
# Request Part
res = requests.post('http://127.0.0.1:5000/hello',json={"name":name,"age":age})
status = res.status_code
print(status)

# Data base Part
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("SELECT * FROM data")
database_data = c.fetchall()
print(database_data)
conn.commit()
conn.close()
