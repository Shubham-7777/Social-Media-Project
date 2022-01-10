from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from posts.views.post import PostView, PostUserView, PostDetailView

app_name = "posts-app"

urlpatterns = [
    path("posts/", PostView.as_view(), name='get-posts'),
 
    path("user-posts/<slug:user>/", PostUserView.as_view(), name="post-user-url"),
    
    path("user-posts-update/<int:post_id>/", PostDetailView.as_view()),
    
]