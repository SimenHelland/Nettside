from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import turtle as trt
from .MÅL_python import mål



views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Type in note!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("MyHome.html", user = current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    

    return jsonify({})

@views.route("/nora-mappe", methods=['GET', 'POST'])
@login_required
def nora():
    trt.setup(800,800,1200)
    trt.hideturtle()
    trt.speed(0)
    trt.pensize(10)

    mål()

    if request.method == "POST":
        sporsmol1 = request.form.get("svar") 

        if sporsmol1 == "22-07-2003":
            flash("Veldig bra!!. Elegant start!!", category='success')
        else:
            flash("Din sviker!! Prøv igjen :(", category="error")

    return render_template("nora_mappe.html") 