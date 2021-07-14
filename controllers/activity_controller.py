from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity


import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

activity_blueprint = Blueprint("activities", __name__)


@activity_blueprint.route('/activity')
def activities():
    activities = activity_repository.select_all()
    return render_template('activity/index.html', activities = activities)

@activity_blueprint.route('/activity/new')
def new_activity():
    return render_template('activity/new.html')

@activity_blueprint.route('/activity', methods =['POST'])
def add_activity():
    name = request.form['activity_name']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    activity = Activity( name, date, time, description)
    activity_repository.save(activity)
    return redirect ('/activity')


@activity_blueprint.route('/activity/<id>')
def show_activity(id):
    activity  = activity_repository.select(id)
    all_members = activity_repository.members(activity)
    bookings = activity_repository.bookings(activity)
    return render_template('activity/show.html', activity = activity , members = all_members, bookings = bookings)


@activity_blueprint.route('/activity/<id>/edit')
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template('activity/edit.html', activity = activity)

@activity_blueprint.route('/activity/<id>', methods =['POST'])
def update_activity(id):
    activity_name = request.form['activity_name']
    date = request.form['date']
    time =request.form['time']
    description = request.form['description']
    activity = Activity(activity_name, date, time, description, id)
    activity_repository.update(activity)
    return redirect('/activity')

@activity_blueprint.route('/activity/<id>/delete')
def delete_activity(id):
    activity_repository.delete(id)
    return redirect('/activity')

@activity_blueprint.route('/activity/search' , methods = ['POST'])
def search_activity():
    info_to_search = request.form['search']
    result = activity_repository.search(info_to_search)
    return render_template('activity/search.html' , activities = result)
