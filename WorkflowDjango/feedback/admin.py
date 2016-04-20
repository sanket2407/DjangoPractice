from django.contrib import admin

# Register your models here.
from .models import FeedBack
from .forms import FeedBackForm

class FeedBackAdmin(admin.ModelAdmin):

# defining format to record detail

	list_display = ["__unicode__", "feedback"]

# adding model directly to the admin

	# class Meta:
	# 	model = FeedBack

# we are going to add form here instead of direct model
	form = FeedBackForm


admin.site.register(FeedBack, FeedBackAdmin)



