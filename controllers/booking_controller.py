from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
from models.booking import Booking
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

booking_blueprint = Blueprint("booking", __name__)

@booking_blueprint.route('/booking/new')
def new_booking():
    all_members = member_repository.select_all()
    all_activities = activity_repository.select_all()
    return render_template('booking/new.html', members =all_members, activities = all_activities)

@booking_blueprint.route('/', methods = ['POST'])
def add_booking():
    member_id = request.form['member']
    activity_id = request.form['activity']
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity)
    booking_repository.save(booking)
    return redirect('/') 

@booking_blueprint.route('/booking/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template( 'booking/show.html', booking = booking)
