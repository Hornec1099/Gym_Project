import unittest
from models.booking import Booking
from models.member import Member
from models.activity import Activity

class TestBooking(unittest.TestCase):
    
    def setUp(self):
        self.member = Member( "Steve the Pirate", 35)
        self.activity= Activity( "Dodeball 101", "10/07/2021", "14:00", "Dodge, Duck, Dip, Dive and Dodge")
        self.booking = Booking ( self.member, self.activity)


    def test_booking_has_member(self):
        self.assertEqual(self.member, self.booking.member_id)

    def test_booking_has_activity(self):
        self.assertEqual( self.activity , self.booking.activity_id)