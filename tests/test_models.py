from unittest import TestCase
from models import Room, Hotel, Booking

class TestModelIs(TestCase):
    def setUp(self) -> None:
        self.booking = Booking()
        self.hotel = Hotel()
        self.room = Room()

    def test_hotel(self):
        self.assertIsNotNone(self.hotel.create)
        self.assertTrue(self.room.create)

    def test_room(self):
        self.assertIsNotNone(self.room.hotel)
        self.assertTrue(self.room.hotel)

    def test_booking(self):
        self.assertIsNotNone(self.booking.create)
        self.assertIsNotNone(self.booking.create)

    def test_room_booking(self):
        self.assertIsNotNone(self.booking.room)


    def test_register_hotel_true(self):
        self.assertIsNotNone(self.hotel.create)    

    def tearDown(self):
        self.booking = Booking()
        self.hotel = Hotel()
        self.room = Room()
        print("Collapse test")       
