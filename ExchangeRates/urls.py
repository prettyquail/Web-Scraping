from . import views
from django.urls import path

urlpatterns = [
    path("", views.main, name="main"),
    path("one/", views.index, name="index"),
    path("two/", views.indextwo, name="indextwo"),
    path("three/", views.indexthree, name="indexthree"),
]
