from flask import Blueprint, request, redirect, url_for
from models import db, Player, BattingStatistics

delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/delete_player', methods=['POST'])
def delete_player():
    player_ids = request.form.getlist('delete_player')
    if player_ids:
        for player_id in player_ids:
            player = Player.query.get(player_id)
            if player:
                db.session.delete(player)
        db.session.commit()
    return redirect(url_for('read.index'))

@delete_bp.route('/delete_stat', methods=['POST'])
def delete_stat():
    stat_ids = request.form.getlist('delete_stat')
    if stat_ids:
        for stat_id in stat_ids:
            stat = BattingStatistics.query.get(stat_id)
            if stat:
                db.session.delete(stat)
        db.session.commit()
    return redirect(url_for('read.index'))
