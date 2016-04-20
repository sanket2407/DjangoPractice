from django.contrib import admin

# Register your models here.
from .models import FeedBack

class FeedBackAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "feedback"]
	class Meta:
		model = FeedBack

admin.site.register(FeedBack, FeedBackAdmin)