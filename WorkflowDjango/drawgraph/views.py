from django.shortcuts import render
import urllib2

# Create your views here.
def draw(request):

	# getting data from service running on localhost 3000 with node.js
	data = " None from call "
	# for python version 2.X
	#data = urllib2.urlopen("http://localhost:3000/users").read()

	# for python version 3.X
	# import urllib.request
	# json_data = urllib.request.urlopen("http://localhost:3000/users").read()

	context = {
	"data" : data,
	}
	return render(request, "graph.html", context)
