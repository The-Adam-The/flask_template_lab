from flask import render_template, request
from modules.event import Event
from modules.event_list import event_list, add_event_to_list
from app import app

@app.route('/eventlist')
def index():
    return render_template('index.html', event_list=event_list)

@app.route('/eventlist', methods=['POST'])
def add_event():
    event_name = request.form["event_name"]
    event_date = request.form["event_date"]
    number_of_guests = request.form["number_of_guests"]
    room_name = request.form["room_name"]
    description = request.form["description"]

    recurring = True if request.form["recurring"] == "yes" else False

    new_event = Event(event_date, event_name, number_of_guests, room_name, description, recurring)
    add_event_to_list(new_event)
    return render_template('index.html', event_list=event_list)