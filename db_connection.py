import psycopg2

#Connecting to existing database
conn = psycopg2.connect(
    database="database",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

#Open cursor to perform database operations
cur = conn.cursor()

#query the database
cur.execute("")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)
#Close communication with database
cur.close()
conn.close()