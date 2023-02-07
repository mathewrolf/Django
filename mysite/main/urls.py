from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"), 
path("view/", views.view, name="view"), 
] 

urlpatterns += staticfiles_urlpatterns()
