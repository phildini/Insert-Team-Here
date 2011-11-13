from django.template import Context, loader
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from teams.models import Team
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms
import datetime

class TeamEdit(forms.Form):
	name = forms.CharField(max_length=200, required=False)
	genre = forms.CharField(max_length=100, required=False)
        project_type = forms.CharField(max_length=100, required=False)
        city = forms.CharField(max_length=200, required=False)
        state = forms.CharField(max_length=100, required=False)

def index(request):
	latest_team_list = Team.objects.all().order_by('-creation_date')[:100]
	return render_to_response('teams/index.html', {'latest_team_list': latest_team_list})

def detail(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	return render_to_response('teams/detail.html', {'team': t}, context_instance=RequestContext(request))

def edit(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	if request.method == 'POST':
		form = TeamEdit(request.POST)
		if form.is_valid():
			if form.cleaned_data['name']:
				t.team_name = form.cleaned_data['name']
			if form.cleaned_data['genre']:
                                t.genre = form.cleaned_data['genre']
			if form.cleaned_data['project_type']:
                                t.project_type = form.cleaned_data['project_type']
			if form.cleaned_data['city']:
                                t.city = form.cleaned_data['city']
			if form.cleaned_data['state']:
                                t.state = form.cleaned_data['state']
			t.save()
			return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
	else:
		form = TeamEdit()
	return render_to_response('teams/edit.html', {'form':form, 'team':t}, context_instance=RequestContext(request))

def add(request):
	t = Team(creation_date=datetime.datetime.now())
	t.save()
	if request.method == 'POST':
                form = TeamEdit(request.POST)
                if form.is_valid():
                        if form.cleaned_data['name']:
                                t.team_name = form.cleaned_data['name']
                        if form.cleaned_data['genre']:
                                t.genre = form.cleaned_data['genre']
                        if form.cleaned_data['project_type']:
                                t.project_type = form.cleaned_data['project_type']
                        if form.cleaned_data['city']:
                                t.city = form.cleaned_data['city']
                        if form.cleaned_data['state']:
                                t.state = form.cleaned_data['state']
                        t.save()
                        return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
        else:
                form = TeamEdit()
        return render_to_response('teams/edit.html', {'form':form, 'team':t}, context_instance=RequestContext(request))
