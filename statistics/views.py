from django.shortcuts import render, get_object_or_404
from datetime import date

from statistics.models import NbaGame

def index(request):
    todays_games_list = NbaGame.objects.filter(gamedate=date.today())
    context = {'todays_games_list': todays_games_list}

    return render(request, 'statistics/index.html', context)

def show(request, nba_game_id):
    game = get_object_or_404(NbaGame, pk=nba_game_id)
    away_stat = game.away_team.get_latest_statistic()
    home_stat = game.home_team.get_latest_statistic()
    away_predicted = away_stat.away_ppg * home_stat.home_def_mod
    home_predicted = home_stat.home_ppg * away_stat.away_def_mod
    context = {'game': game, 'away_predicted': away_predicted, 'home_predicted': home_predicted}
    return render(request, 'statistics/show.html', context)
