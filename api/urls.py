from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views as tokenView

from api.views import *

urlpatterns = patterns('',
    
    url(r'^login/', tokenView.obtain_auth_token), 
    url(r'^create/', comment_create,name = 'comment_create'),
    url(r'^list/', discussions_list, name = 'discussions_list'),
    url(r'^discussion/details/$', discussion_search, name='search-discussion'),


    
)
