from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from comments.views.comments import CommentsView, CommentsUpdateView


app_name = 'comments-app'

urlpatterns = [
    path('add-comments/', CommentsView.as_view(), name='post-comment-url'),
    path('update-comments/<int:id>/', CommentsUpdateView.as_view(), name='update-comment-url'),
    
]