from django.urls import path

# from . import views

#  urlpatterns = [
#      path("", views.index, name="index"),
#  ]
from . import views
urlpatterns=[
        path("", views.index, name="index"),
        path("choice", views.Choice, name="decision"),
    ]

