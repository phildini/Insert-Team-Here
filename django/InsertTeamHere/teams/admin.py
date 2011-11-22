from teams.models import Team
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
	fields = ['team_name', 'creation_date']

admin.site.register(Team, TeamAdmin)
