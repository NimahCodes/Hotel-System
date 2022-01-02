
from database import Database
from models import Room, Hotel, Booking

class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        return self.db.hotels.insert(name=name)

    def add_room(self, hotel_id, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        return self.db.rooms.insert(hotel_id=hotel_id, **params)

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
            if self.db.bookings.select(room_id=room_id) == []:
                return None
            return self.db.bookings.select(room_id=room_id)
            

    def book_room(self, room_id, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result

        # Remove the pass statement below and add your implementation there ...
        return self.db.bookings.insert(room_id=room_id, **params)

demiresort = HotelSystem(Database)
print(demiresort.register_hotel(1))
print(demiresort.add_room(1, price = 89, capacity = 34))
print(demiresort.book_room(1, name="um", paid = True))
print(demiresort.get_room(1))