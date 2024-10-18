from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("index", views.index),
    path("posts", views.posts, name="posts"),    
    path("category/<slug:slug>", views.post_by_category, name="post_by_category"),
    path("posts/<slug:slug>",views.post_details,name="post_details"),    
]
