from django.template import Context, loader
from django.shortcuts import render_to_response
from teams.models import Team
from django.http import HttpResponse, Http404


def index(request):
	latest_team_list = Team.objects.all().order_by('-creation_date')[:5]
	return render_to_response('teams/index.html', {'latest_team_list': latest_team_list})

def detail(request, team_id):
	try:
		t = Team.objects.get(pk=team_id)
	except Team.DoesNotExist:
		raise Http404
	return render_to_response('teams/detail.html', {'team': t})

