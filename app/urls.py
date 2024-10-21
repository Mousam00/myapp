from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.signup,name="signup"),
    path('create_post/', views.create_post,name="create_posts"),
]
