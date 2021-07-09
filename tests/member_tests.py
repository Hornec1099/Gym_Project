import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member( "Steve the Pirate", 35)
    
    
    def test_member_has_name(self):
        self.assertEqual("Steve the Pirate", self.member.name)

    def test_member_has_age(self):
        self.assertEqual( 35 , self.member.age)