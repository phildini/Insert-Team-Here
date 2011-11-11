from django.db import models

class Team(models.Model):
	team_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')

class Info(models.Model):
	team = models.ForeignKey(Team)
	genre = models.CharField(max_length=100)
	project_type = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000)
	
class Location(models.Model):
	team = models.ForeignKey(Team)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=100)
	

