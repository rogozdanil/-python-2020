from django.urls import path

from . import views


urlpatterns = [
    path("", views.CommandsView.as_view())
]