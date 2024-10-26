# create.py
from flask import Blueprint, request, redirect, url_for
from models import db, Player, BattingStatistics

create_bp = Blueprint('create', __name__)

@create_bp.route('/add_player', methods=['POST'])
def add_player():
    player_ID = request.form['player_ID']
    player_name = request.form['player_name']
    birth_date = request.form['birth_date']
    birth_place = request.form['birth_place']
    team_ID = request.form['team_ID']
    stats_ID = request.form['stats_ID']

    new_player = Player(
        player_ID=player_ID,
        player_name=player_name,
        birth_date=birth_date,
        birth_place=birth_place,
        team_ID=team_ID,
        stats_ID=stats_ID
    )
    db.session.add(new_player)
    db.session.commit()
    return redirect(url_for('read.index'))

@create_bp.route('/add_stat', methods=['POST'])
def add_stat():
    AVG = request.form['AVG']
    Hits = request.form['Hits']
    HR = request.form['HR']
    RBI = request.form['RBI']
    new_stat = BattingStatistics(AVG=AVG, Hits=Hits, HR=HR, RBI=RBI)
    db.session.add(new_stat)
    db.session.commit()
    return redirect(url_for('read.index'))
