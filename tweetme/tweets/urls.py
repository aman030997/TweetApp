from .views import (
	TweetListView,
	TweetDetailView,
	TweetCreateView,
	TweetUpdateView,
	TweetDeleteView
	)
from django.urls import path
from django.conf.urls import include,url
from django.views.generic.base import RedirectView

app_name = 'tweet'

urlpatterns = [
	url(r'^$',RedirectView.as_view(url="/")),
	url(r'^search/$',TweetListView.as_view(),name='list'),
	url(r'^create/$',TweetCreateView.as_view(),name='create'),
	url('^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'),
	url('^(?P<pk>\d+)/update/$',TweetUpdateView.as_view(),name='update'),
	url('^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name='delete'),

] 
