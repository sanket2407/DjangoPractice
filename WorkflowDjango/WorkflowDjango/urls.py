from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^feedback/$', 'feedback.views.feedBackView', name='feedBackView'),
    url(r'^graph/$', 'drawgraph.views.draw', name='draw'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
