from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=420)
    def __str__(self):
        return self.team_name
    #maybe a picture later on

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    member_name = models.CharField(max_length = 420)
#members default to being opted in
    leads_events = models.BooleanField(default=True)
    #maybe a picture later on

    def __str__(self):
        return self.member_name
