from django.shortcuts import render

def home(request):
	title = "Welcome"
	if request.user.is_authenticated():
		title = str(request.user)

	context = {
		"title": title
	}

	return render(request, "home.html", context)