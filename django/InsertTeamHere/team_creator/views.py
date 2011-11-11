from django.http import HttpResponse

def index(request):
	return HttpResponse("Greetings program! You've reached the Team Creation page!.")

def detail(request, team_id):
	return HttpResponse("You are now looking at the team with TeamID %s." % team_id)

