from django.db import models

# Create your models here.
class NbaConference(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'nba_conferences'

class NbaDivision(models.Model):
    conference = models.ForeignKey(NbaConference)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'nba_divisions'

class NbaTeam(models.Model):
    nba_division = models.ForeignKey(NbaDivision)
    city = models.CharField(max_length=200)
    mascot = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)

    def __unicode__(self):
        return self.city + ' ' + self.mascot

    class Meta:
        db_table = 'nba_teams'

class NbaGame(models.Model):
    home_team = models.ForeignKey(NbaTeam, related_name='home_team')
    away_team = models.ForeignKey(NbaTeam, related_name='away_team')
    gamedate = models.DateField()
    gametime = models.TimeField()
    season = models.CharField(max_length=200)

    class Meta:
        db_table = 'nba_games'
