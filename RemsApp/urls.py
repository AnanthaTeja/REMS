from django.urls import path
from . import views
from django.contrib.auth import views as dc

urlpatterns = [
    path("", views.home, name="hm"),
    path("abt/", views.about, name="ab"),
    path("cnt/", views.contact, name="ct"),
    path("reg/", views.register, name="rg"),
    path("lgn/", dc.LoginView.as_view(template_name="html/login.html"), name="lg"),
]
