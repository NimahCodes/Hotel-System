import unittest
from database import Table

tables = Table()

class TestDataBase(unittest.TestCase):
    def test_table_fields(self):
        result = tables.fields
        self.assertIsNotNone(result)

    def test_data_type(self):
        result = type(tables.data)
        self.assertEqual(result, dict)

    def test_insert(self):
        result = tables.insert
        self.assertIsNotNone(result)    

    def test_select(self):
        result = tables.select
        self.assertIsNotNone(result)

    def test_table_true(self):
        result = tables.fields
        self.assertIsNotNone(result)       

              