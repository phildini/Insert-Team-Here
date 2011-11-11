from django.template import Context, loader
from teams.models import Team
from django.http import HttpResponse


def index(request):
	latest_team_list = Team.objects.all().order_by('-creation_date')[:5]
	temp = loader.get_template('teams/index.html')
	cont = Context({
		'latest_team_list': latest_team_list,
	})
	return HttpResponse(temp.render(cont))

def detail(request, team_id):
	return HttpResponse("You are now looking at the team with TeamID %s." % team_id)

