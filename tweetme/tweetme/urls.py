"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from tweets.views import TweetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TweetListView.as_view(),name='home'),
    path('',include('accounts.urls',namespace='profiles')),
    path('tweet/',include('tweets.urls',namespace='tweet')),
    path('api/tweet/',include('tweets.api.urls',namespace='tweet-api')),

]

if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))