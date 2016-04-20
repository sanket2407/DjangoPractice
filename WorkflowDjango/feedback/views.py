from django.shortcuts import render
from .forms import FeedBackForm

# Create your views here.

def feedBackView(request):

	title = "FeedBack Form"
	form = FeedBackForm(request.POST or None)

	# do something with request
	if request.method == "POST":
		print request.POST
	
	context = {
		"title" : title,
		"form" : form,
	}

	if form.is_valid():	
		# create instance
		instance = form.save(commit=False)

		print instance.email
		print instance.feedback

		# store data in database
		instance.save()

		context = {
		"title" : "Thank you for feedback",
		"form" : form,
		}	

	return render(request, "feedback.html", context)
