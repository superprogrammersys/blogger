from . import views
from django.urls import path
urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("register/",views.register,name="register"),
    path("posts/",views.posts,name="posts"),
    path("posts/<int:pk>/",views.show_post,name="post"),
path("posts/new/",views.new_post,name="new_post"),

]