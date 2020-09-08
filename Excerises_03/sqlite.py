import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employee(
                first text,
                last text,
                pay integer)""")

#c.execute('INSERT INTO employee VALUES ("Jone","Doe",1000)')
c.execute("SELECT * FROM employee ")
conn.commit()
print(c.fetchall())

conn.commit()