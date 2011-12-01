from django.db import models

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


class Team(models.Model):
	team_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
	project_type = models.CharField(max_length=1, choices=PROJ_CHOICES)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=1, choices=STATE_CHOICES)

	def __unicode__(self):
		return self.team_name
