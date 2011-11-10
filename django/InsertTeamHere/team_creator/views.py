from django.http import HttpResponse

def index(request):
	return HttpResponse("Greetings program! You've reached the Team Creation page!.")
