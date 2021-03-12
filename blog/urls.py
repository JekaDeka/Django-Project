from django.urls import path

from .views import blog_post_detail, blog_post_list

urlpatterns = [
    path("", blog_post_list, name="blogpost-list"),
    path("/blogs/<int:pk>/", blog_post_detail, name="blogpost-detail"),
]
