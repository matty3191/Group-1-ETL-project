from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import pandas as pd

conn_url = "postgresql+psycopg2://docker:docker@localhost/database"

engine = create_engine(conn_url)

db = scoped_session(sessionmaker(bind=engine))

d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(d)

df.to_sql(name="df", con=engine, index=True, if_exists="append")

# query_rows = db.execute("SELECT * FROM anyTableName").fetchall()
# for register in query_rows:
#     print(f"{register.col_1_name}, {register.col_2_name}, ..., {register.col_n_name}")
