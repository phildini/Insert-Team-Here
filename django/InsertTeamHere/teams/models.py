from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES=(
	('AL', 'Alabama'),
	('AK','Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DE', 'Delaware'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI','Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('KY', 'Kentucky'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),
	('ND', 'North Dakota'),
	('OH', 'Ohio'),
	('OK', 'Oklahoma'),
	('OR', 'Oregon'),
	('PA', 'Pennsylvania'),
	('RI', 'Rhode Island'),
	('SC', 'South Carolina'),
	('SD', 'South Dakota'),
	('TN', 'Tennessee'),
	('TX', 'Texas'),
	('UT', 'Utah'),
	('VT', 'Vermont'),
	('VA', 'Virginia'),
	('WA', 'Washington'),
	('WV', 'West Virginia'),
	('WI', 'Wisconsin'),
	('WY', 'Wyoming'),
)
GENRE_CHOICES=(
	('Action','Action'),
	('Adventure','Adventure'),
	('Platformer','Platformer'),
	('Puzzle','Puzzle'),
	('Strategy','Strategy'),
	('RPG','RPG')
)
PROJ_CHOICES=(
	('Video Game','Video Game'),
	('Web Application','Web Application'),
	('Multimedia Project', 'Multimedia Project')
)

class Roles(models.Model):
	talent=models.CharField(max_length=200)
	experience=models.CharField(max_length=200)

class Team(models.Model):
	# ******************
	members=models.ManyToManyField(User)
	#owner=models.ForeignKey(User)
	# *************
	team_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
	project_type = models.CharField(max_length=1, choices=PROJ_CHOICES)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=1, choices=STATE_CHOICES)
	
	seeking=models.ManyToManyField(Roles)

	def __unicode__(self):
		return self.team_name

#class Team_Members(models.Model):
#	members=models.ForeignKey(User)
#	team=models.ForeignKey(Team)

