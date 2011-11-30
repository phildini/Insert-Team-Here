from teams.models import Team
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ('creation_date','team_name',('project_type','genre'),('city', 'state'))}),
    ]

admin.site.register(Team, TeamAdmin)
