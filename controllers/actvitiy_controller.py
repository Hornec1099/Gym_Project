from datetime import date
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity


import repositories.activity_repository as activity_repository

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