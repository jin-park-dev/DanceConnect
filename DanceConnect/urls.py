"""DanceConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls import url



from .views import (
    HomeView,
    MyHomeListView,
)

# from .settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('', HomeView.as_view(), name="home"),
    path('events/', include('events.urls', namespace='events')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('search/', include('search.urls', namespace='search')),
    path('friends/', include('friends.urls', namespace='friends')),
    path('venders/', include('venders.urls', namespace='venders')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('home/', MyHomeListView.as_view(), name='my_home'),

    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),

    url(r'^notifications/', include('notify.urls', 'notifications')),


    # path('profiles/', include('django.contrib.auth.urls')), # TODO: I remember fixing this issue before with another url. Maybe It was different issue?


]

# if DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#                       re_path(r'__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
