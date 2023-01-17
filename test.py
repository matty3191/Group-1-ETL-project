import unittest
import pandas as pd
from io import StringIO

class TestDataProcessing(unittest.TestCase):

# Test that the code correctly reads a CSV file
    def test_csv_file_reading(self):
        csv_data = '''DateTime,Cafe Branch,Name,Product,Price,Payment Method,Card Number
25-08-2021 09:00:00,Chesterfield,John Doe,Coffee,3.50,Visa,1234-5678-9012-3456'''
        raw_data = StringIO(csv_data)
        df = pd.read_csv(raw_data)
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)


# Test that the code correctly raises an exception for invalid file format
    def test_invalid_file_format(self):
        raw_data = "chesterfield_25-08-2021_09-00-00.txt"
        with self.assertRaises(ValueError) as cm:
            if raw_data.endswith(".csv"):
                df = pd.read_csv(raw_data)
            else:
                raise ValueError("Invalid file format")
        self.assertEqual(str(cm.exception), "Invalid file format")


        # Test that the code correctly renames the columns
    def test_column_renaming(self):
        csv_data = '''DateTime,Cafe Branch,Name,Product,Price,Payment Method,Card Number
25-08-2021 09:00:00,Chesterfield,John Doe,Coffee,3.50,Visa,1234-5678-9012-3456'''
        raw_data = StringIO(csv_data)
        df = pd.read_csv(raw_data)
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
        self.assertEqual(list(df.columns), column_names)


# Test that the code correctly drops the specified columns
    def test_column_dropping(self):
        csv_data = '''DateTime,Cafe Branch,Name,Product,Price,Payment Method,Card Number
25-08-2021 09:00:00,Chesterfield,John Doe,Coffee,3.50,Visa,1234-5678-9012-3456'''
        raw_data = StringIO(csv_data)
        df = pd.read_csv(raw_data)
        to_drop = [
            'Card Number',
            'Name'
        ]
        df.drop(columns=to_drop, inplace=True)
        self.assertNotIn('Card Number', df.columns)
        self.assertNotIn('Name', df.columns)

