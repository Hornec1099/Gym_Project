from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member


import repositories.member_repository as member_repository 

member_blueprint = Blueprint( "members", __name__)

@member_blueprint.route("/members")
def index():
    members = member_repository.select_all()
    return render_template( "members/index.html", all_members = members)


@member_blueprint.route("/members/new")
def new_member_form():
    return render_template("members/new.html")

@member_blueprint.route('/members', methods =['POST'])
def create_member():
    name = request.form['name']
    age = request.form['age']
    member = Member(name, age)
    member_repository.save(member)
    return redirect( "/members")


@member_blueprint.route('/members/<id>')
def show_member(id):
    member = member_repository.select(id)
    activities = member_repository.activities(member)
    return render_template('members/show.html', member = member, activities = activities)


@member_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member = member)



@member_blueprint.route('/members/<id>', methods=['POST'])
def alter_member(id):
    name = request.form['edited_name']
    age = request.form['edited_age']
    member = Member(name, age, id)
    member_repository.update(member)
    return redirect ('/members')


@member_blueprint.route('/members/<id>/delete')
def delete_member_id(id):
    member_repository.delete(id)
    return redirect('/members')