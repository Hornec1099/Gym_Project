from db.run_sql import run_sql

from models.member import Member
from models.activity import Activity

import repositories.activity_repository as activity_repository

def save(member):
    sql = "INSERT INTO members(name, age) VALUES (%s, %s) RETURNING id"
    values = [member.name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def select_all():
    members = []
    sql = " SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['age'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'] , result['age'], result['id'])
    return member


def activities(member):
    activities = []
    sql = "SELECT activities.* FROM activities INNER JOIN bookings ON bookings.activity_id  = activities.id  WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for result in results:
        activity = Activity(result['name_of_activity'], result['day_of'], result['time_of'],result['description'],result['id'])
        activities.append(activity)
    return activities


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def update(member):
    sql = "UPDATE members SET (name, age) = (%s, %s) WHERE id = %s"
    values = [member.name, member.age, member.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def search(to_search):
    members_found = []
    sql = "SELECT * FROM members WHERE name = %s OR age = %s"
    values = [to_search, to_search]
    results = run_sql(sql,values)
    for result in results:
        member = Member (result['name'],result['age'],result['id'])
        members_found.append(member)
    return members_found