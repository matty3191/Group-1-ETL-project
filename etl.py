import pandas as pd

#Extraction - to be ammended for postgresql database from docker and automated to be done at certain times of the day
raw_data = "chesterfield_25-08-2021_09-00-00.csv"

if raw_data.endswith(".csv"):
    df = pd.read_csv(raw_data)
else:
    print("Invalid file format")

#Transformation
