from flask import Blueprint, request, redirect, url_for
from models import db, Player, BattingStatistics

update_bp = Blueprint('update', __name__)

@update_bp.route('/update_player/<int:id>', methods=['POST'])
def update_player(id):
    player = Player.query.get_or_404(id)
    player.player_name = request.form['player_name']
    player.birth_date = request.form['birth_date']
    player.birth_place = request.form['birth_place']
    player.team_ID = request.form['team_ID']
    player.stats_ID = request.form['stats_ID']
    db.session.commit()
    return redirect(url_for('read.index'))

@update_bp.route('/update_stat/<int:id>', methods=['POST'])
def update_stat(id):
    stat = BattingStatistics.query.get_or_404(id)
    stat.AVG = request.form['AVG']
    stat.Hits = request.form['Hits']
    stat.HR = request.form['HR']
    stat.RBI = request.form['RBI']
    db.session.commit()
    return redirect(url_for('read.index'))
