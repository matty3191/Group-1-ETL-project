import pandas as pd

#Extraction - to be ammended for postgresql database from docker and automated to be done at certain times of the day
raw_data = "chesterfield_25-08-2021_09-00-00.csv"

if raw_data.endswith(".csv"):
    df = pd.read_csv(raw_data)
else:
    print("Invalid file format")

#Transformation
column_names = [
    'DateTime',
    'Cafe Branch',
    'Name',
    'Product',
    'Price',
    'Payment Method',
    'Card Number'
]

df.columns = column_names

#Dropping Card Number
to_drop = [
    'Card Number',
    'Name'
]

df.drop (columns = to_drop, inplace=True)
df.head()

#Creating new Date and Time columns 
df[['Date','Time']] = df.DateTime.str.split(" ",expand=True,)
df.head()

to_drop = [
    'DateTime',
]

df.drop (columns = to_drop, inplace=True)
df.head()


