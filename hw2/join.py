# join.py
from flask import Blueprint, render_template
from sqlalchemy import text
from models import db

join_bp = Blueprint('join', __name__)

@join_bp.route('/join_data')
def join_data():
    sql_query = text("""
        SELECT Player.player_name, Team.team_name, BattingStatistics.AVG, BattingStatistics.Hits
        FROM Player
        JOIN Team ON Player.team_ID = Team.team_ID
        JOIN BattingStatistics ON Player.stats_ID = BattingStatistics.stats_ID
    """)
    result = db.session.execute(sql_query)
    joined_data = result.fetchall()

    return render_template('join_data.html', data=joined_data)
