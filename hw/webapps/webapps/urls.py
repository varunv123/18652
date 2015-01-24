from django.conf.urls import patterns, include, url

# Default URL routes file for the controller.  Here we are simply matching
# URL patterns by regular expression, and defining the full route elsewhere by
# including the route file for intro application.
urlpatterns = patterns('',
    url(r'^intro/', include('intro.urls')),
    url(r'', include('intro.urls')),
)
