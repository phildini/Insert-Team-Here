from django.template import Context, loader
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from teams.models import Team
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
import datetime

STATE_CHOICES=(
	('None', '--State--'),
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
	('None', '--Genre--'),
	('Action','Action'),
	('Adventure','Adventure'),
	('Platformer','Platformer'),
	('Puzzle','Puzzle'),
	('Strategy','Strategy'),
	('RPG','RPG')
)

PROJ_CHOICES=(
	('None', '--Project Type--'),
	('Video Game','Video Game'),
	('Web Application','Web Application'),
	('Multimedia Project', 'Multimedia Project')
)

class TeamEdit(forms.Form):
	name = forms.CharField(max_length=200, required=False)
	genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False)
	project_type = forms.ChoiceField(choices=PROJ_CHOICES, required=False)
	city = forms.CharField(max_length=200, required=False)
	state = forms.ChoiceField(choices=STATE_CHOICES, required=False)
	
class SearchBar(forms.Form):
	state= forms.ChoiceField(choices=STATE_CHOICES)
	genre= forms.ChoiceField(choices=GENRE_CHOICES)
	project_type=forms.ChoiceField(choices=PROJ_CHOICES)

def index(request):
	latest_team_list = Team.objects.all()
	if request.method=='GET':
		form = SearchBar(request.GET)
		if form.is_valid():
			curr_state=form.cleaned_data['state']
			curr_genre=form.cleaned_data['genre']
			curr_proj=form.cleaned_data['project_type']
			if curr_state!='None':
				latest_team_list=latest_team_list.filter(state__exact=curr_state)
			if curr_genre!='None':
				latest_team_list=latest_team_list.filter(genre__exact=curr_genre)
			if curr_proj!='None':
				latest_team_list=latest_team_list.filter(project_type__exact=curr_proj)
		return render_to_response('teams/index.html', {'latest_team_list':latest_team_list.order_by('-creation_date'), 'form':form,})
	else:
		form = SearchBar()
	return render_to_response('teams/index.html', {'latest_team_list': latest_team_list.order_by('-creation_date'), 'form':form,})

def detail(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	u_mem='None'
	if request.user.is_authenticated():
		if t.members.filter(username__exact=request.user):
			u_mem=t.members.get(pk=request.user.id)
	return render_to_response('teams/detail.html', {'team': t, 'mem': u_mem}, context_instance=RequestContext(request))

@login_required
def edit(request, team_id):
	t = get_object_or_404(Team, pk=team_id)
	
	class TeamEdit_specific(forms.Form):
		name = forms.CharField(max_length=200, required=False, initial=t.team_name)
		genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False, initial=t.genre)
		project_type = forms.ChoiceField(choices=PROJ_CHOICES, required=False, initial=t.project_type)
		city = forms.CharField(max_length=200, required=False, initial=t.city)
		state = forms.ChoiceField(choices=STATE_CHOICES, required=False, initial=t.state)
		
	if request.method == 'POST':
		form = TeamEdit_specific(request.POST)
		if form.is_valid():
			if form.cleaned_data['name']!=t.team_name:
				t.team_name = form.cleaned_data['name']
			if form.cleaned_data['genre']!='None' or form.cleaned_data['genre']!=t.genre:
				t.genre = form.cleaned_data['genre']
			if form.cleaned_data['project_type']!='None' or form.cleaned_data['project_type']!=t.project_type:
				t.project_type = form.cleaned_data['project_type']
			if form.cleaned_data['city']:
				t.city = form.cleaned_data['city']
			if form.cleaned_data['state']!=t.state:
				if form.cleaned_data['state']=='None':
					t.state='None'
				else:
					t.state = form.cleaned_data['state']
			t.save()
			return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
	else:
		form = TeamEdit_specific()
		#form.name.value=t.team_name
	return render_to_response('teams/edit.html', {'form':form, 'team':t}, context_instance=RequestContext(request))

@login_required
def add(request):
	t = Team(creation_date=datetime.datetime.now())
	t.save()
	if request.method == 'POST':
                form = TeamEdit(request.POST)
                if form.is_valid():
                        if form.cleaned_data['name']:
                                t.team_name = form.cleaned_data['name']
                        if form.cleaned_data['genre']!='None':
                                t.genre = form.cleaned_data['genre']
                        if form.cleaned_data['project_type']!='None':
                                t.project_type = form.cleaned_data['project_type']
                        if form.cleaned_data['city']:
                                t.city = form.cleaned_data['city']
                        if form.cleaned_data['state']!='None':
                                t.state = form.cleaned_data['state']
                        t.owner=get_object_or_404(User, pk=request.user.id)
                        t.save()
                        return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
        else:
                form = TeamEdit()
        return render_to_response('teams/edit.html', {'form':form, 'team':t}, context_instance=RequestContext(request))

@login_required
def join(request, team_id):
	t= get_object_or_404(Team, pk=team_id)
	curr_user= get_object_or_404(User, pk=request.user.id)
	if curr_user in t.members.all():
		return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
	else:
		t.members.add(curr_user)
		t.save()
		return HttpResponseRedirect(reverse('teams.views.detail', args=(t.id,)))
