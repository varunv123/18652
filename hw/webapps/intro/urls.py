from django.conf.urls import patterns, include, url

# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns('',
    url(r'^home$', 'intro.views.home'),
    url(r'^get-list$', 'intro.views.get_list'),
    url(r'^post-message$', 'intro.views.post_message'),
    url(r'^enter-chat$', 'intro.views.enter_chat'),
    url(r'^$', 'intro.views.home'),
)
