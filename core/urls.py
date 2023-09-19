# from django import views
from django.urls import path
from core.views import index
from core import views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("sign-up/", views.register_view, name="sign-up")
]
