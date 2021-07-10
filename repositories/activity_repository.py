from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member


def save(activity):
    sql = "INSERT INTO activities (name_of_activity, day_of, time_of, description) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [activity.name, activity.date, activity.time, activity.description]
    results = run_sql(sql,values)
    activity.id = results[0]['id']
    return activity

def select(id):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    activity = None
    result = run_sql(sql,values)[0]

    if result is not None:
        activity = Activity(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])

    return activity    

def select_all():
    activities = []
    sql = "SELECT * FROM activities "
    results = run_sql (sql)

    for result in results:
        activity = Activity(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])
        activities.append(activity)
    
    return activities

def update(activity):
    sql = "UPDATE activities SET (name_of_activity, day_of, time_of, description) = (%s, %s,%s,%s) WHERE id = %s"
    values = [activity.name , activity.date, activity.time, activity.description, activity.id]
    result =run_sql(sql, values)

    activity1 = Activity(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])
    return activity1


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.members_id = members.id WHERE activity_id = %s"
    values = [id]
    results = run_sql (sql, values)

    for result in results:
        member = Member(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])
        members.append(member)

    return members