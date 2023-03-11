from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("profile/",views.profile,name="profile"),
    path("home/",views.home,name="home"),
    path("Login/",views.Login,name="Login"),
    path("Logout/",views.Login,name="Logout"),
    path("Register/",views.Register,name="Register"),
    path("Resindex/",views.Resindex,name="Resindex"),
    path("Post/",views.Post,name="Post"),
]
