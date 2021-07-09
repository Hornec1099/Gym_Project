import unittest
from models.activity import Activity

class TestActivity (unittest.TestCase):

    def setUp(self):
       self.activity = Activity( "Dodgeball 101", "10/07/2021", "14:00", "Dodge, Duck, Dip, Dive and Dodge")
    
    def test_activity_has_name(self):
        self.assertEqual("Dodgeball 101", self.activity.name)

    def test_activity_has_date(self):
        self.assertEqual("10/07/2021", self.activity.date)

    def test_activity_has_time(self):
        self.assertEqual("14:00", self.activity.time)

    def test_activity_has_description(self):
        self.assertEqual("Dodge, Duck, Dip, Dive and Dodge", self.activity.description)