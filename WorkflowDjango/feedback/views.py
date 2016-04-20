from django.shortcuts import render

# Create your views here.

def feedBackView(request):

	title = "FeedBack Form"
	context = {
		"title" : title
	}

	return render(request, "feedback.html", context)
