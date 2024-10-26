from flask import Blueprint, render_template
from models import Player, Team, BattingStatistics

read_bp = Blueprint('read', __name__)

@read_bp.route('/')
def index():
    players = Player.query.all()
    teams = Team.query.all()
    stats = BattingStatistics.query.all()
    return render_template('index.html', players=players, teams=teams, stats=stats)
