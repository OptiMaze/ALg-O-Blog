from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from articles import views as article_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',article_views.article_lists,name = 'home'),
    path('articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)