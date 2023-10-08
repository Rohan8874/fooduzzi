# from django import views
from django.urls import path
from core.views import index
from core import views
from . import views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("sign-up/", views.register_view, name="sign-up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("contact/",views.contact,name="contact"),
    path("account/", views.account,name="account")
]
