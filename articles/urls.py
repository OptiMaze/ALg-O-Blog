from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$',views.article_lists,name='list'),
    url(r'^create/$',views.create,name='create'),
    url(r'^userArticles/$',views.userArticles,name = 'userArticles'),
    url(r'^(?P<slug>[\w-]+)/$',views.delete,name='delete'),
    url(r'^wallah/(?P<slug>[\w-]+)/$',views.article_details,name='detail'),
    
]   
