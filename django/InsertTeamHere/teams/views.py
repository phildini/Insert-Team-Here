from django.template import Context, loader
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from teams.models import Team
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms

class TeamEdit(forms.Form):
	name = forms.CharField(max_length=200)
	genre = forms.CharField(max_length=100)
        project_type = forms.CharField(max_length=100)
        city = forms.CharField(max_length=200)
        state = forms.CharField(max_length=100)

def index(request):
	latest_team_list = Team.objects.all().order_by('-creation_date')[:5]
	return render_to_response('teams/index.html', {'latest_team_list': latest_team_list})

def detail(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	return render_to_response('teams/detail.html', {'team': t}, context_instance=RequestContext(request))

def edit(request, team_id):
	if request.method == 'POST':
		form = TeamEdit(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('index')
	else:
		form = TeamEdit()
	return render_to_response('teams/edit.html', {'form':form},)
