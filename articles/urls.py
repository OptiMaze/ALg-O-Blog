from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.article_lists),
    url(r'^(?P<slug>[\w-]+)$',views.article_details),
]
