from django.template import Context, loader
from django.template import RequestContext
from django.core import reverse
from django.shortcuts import render_to_response, redner_to_response
from teams.models import Team, Info
from django.http import HttpResponse, Http404, HttpResponseRedirect


def index(request):
	latest_team_list = Team.objects.all().order_by('-creation_date')[:5]
	return render_to_response('teams/index.html', {'latest_team_list': latest_team_list})

def detail(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	return render_to_response('teams/detail.html', {'team': t}, context_instance=RequestContext(request))

