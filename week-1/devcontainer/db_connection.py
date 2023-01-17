import psycopg2

# Connecting to existing database
conn = psycopg2.connect(
    database="postgres", user="docker", password="docker", host="localhost"
)

# Open cursor to perform database operations
cur = conn.cursor()

# Creating table as per requirement
sql = """CREATE TABLE PEOPLE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)"""
# query the database
cur.execute(sql)

conn.commit()

# rows = cur.fetchall()

# if not len(rows):
#     print("Empty")
# else:
#     for row in rows:
#         print(row)
# Close communication with database
cur.close()
conn.close()
