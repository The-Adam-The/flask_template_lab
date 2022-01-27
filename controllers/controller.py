from flask import render_template
from modules.event_list import event_list
from app import app

@app.route('/eventlist')
def index():
    return render_template('index.html', event_list=event_list)
