import unittest
from hotel_system import HotelSystem
from database import Database

db = Database()
hotelsystem = HotelSystem(db)

class TestHotelSystem(unittest.TestCase):
    def test_register_hotel(self):
        result = hotelsystem.register_hotel
        self.assertIsNotNone(result)

    def test_add_room(self):
        result = hotelsystem.add_room
        self.assertIsNotNone(result)

    def test_get_room(self):
        result = hotelsystem.get_room
        self.assertIsNotNone(result)    

    def test_book_room(self):
        result = hotelsystem.book_room
        self.assertIsNotNone(result)  

    def test_register_true(self):
        result = hotelsystem.register_hotel
        self.assertTrue(result)          