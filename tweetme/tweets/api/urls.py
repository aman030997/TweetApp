from django.conf.urls import include,url

from django.views.generic.base import RedirectView

from .views import (
	TweetCreateAPIView,
	TweetListAPIView
	)
app_name = 'tweet-api'
urlpatterns = [
	url(r'^$',TweetListAPIView.as_view(),name='list'),
	url(r'^create/$',TweetCreateAPIView.as_view(),name='create'),
]