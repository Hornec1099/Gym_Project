from db.run_sql import run_sql

from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [ booking.member.id,booking.activity.id]
    result =run_sql(sql,values)
    booking.id  = result[0]['id']
    return booking

def select_all():
    bookings = []
    sql = " SELECT * FROM bookings"
    results = run_sql(sql) 
     
    for result in results:
        member = member_repository.select(result['member_id'])
        activity = activity_repository.select(result['activity_id'])
        booking = Booking( member , activity, result['id'])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql , values)
    
    if result is not None:
        booking = Booking( result['member_id'], result['activity_id'])
    
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql (sql)

def delete(id):
    sql = "DELETE * FROM bookings WHERE id = %s"
    values  = [id]
    run_sql(sql,values)
