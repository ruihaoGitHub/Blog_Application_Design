"""Defines URL patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('signup/', views.signup, name='signup'),
]
