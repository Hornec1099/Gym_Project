from db.run_sql import run_sql

from models.booking import Booking
from models.activity import Activity
from models.member import Member

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
    sql = "SELECT * FROM bookings WHERE id =%s"
    values = [id]
    result  = run_sql(sql, values)[0]

    if result is not None:
        member = member_repository.select(result['member_id'])
        activity = activity_repository.select(result['activity_id'])
        booking = Booking(member,activity,id)
        
    return booking

def select_activity(booking):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [booking.activity.id]
    result = run_sql(sql , values)
    
    if result is not None:
        activity = Activity(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])     
    return activity

def select_member(booking):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    result = run_sql(sql , values)[0]
    
    if result is not None:
        member = Member(result['name'] , result['age'], result['id'])    
    return member

def check_booking(booking):
    checked_booking = None
    sql ="SELECT * FROM bookings WHERE member_id = %s AND activity_id = %s"
    values = [booking.member.id, booking.activity.id]
    results = run_sql(sql,values)
    for result in results:
        if result is not None:
            member = member_repository.select(result['member_id'])
            activity = activity_repository.select(result['activity_id'])
            checked_booking = Booking( member , activity, result['id'])
    return checked_booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql (sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values  = [id]
    run_sql(sql,values)
