from models.activity import Activity
from models.booking import Booking
from models.member import Member

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

member_repository.delete_all()
activity_repository.delete_all()

activity1 = Activity( "Dodgeball 101", "07/20/2021", "14:00", "Dodge, Duck, Dip, Dive and Dodge")
activity2 = Activity( "How to be a Pirate", "07/15/2021","18:00", "Sail the Seven Seas")
activity3 = Activity( "Cheerleading Essentials", "07/12/2021", "12:00", "Handstands and girl talk")

activity_repository.save(activity1)
activity_repository.save(activity2)
activity_repository.save(activity3)


member1 = Member( "Steve the Pirate", 35)
member2 = Member( "Gordon", 49)
member3 = Member( "White Goodman", 32)

member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)


booking1 = Booking( member1 , activity2 )
booking2 = Booking( member3 , activity3 )
booking3 = Booking( member2 , activity1 )