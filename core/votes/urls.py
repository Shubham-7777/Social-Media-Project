from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from votes.views.vote import PostVoteView, PostUpdateView


app_name = "votes-app"

urlpatterns = [
    path("post-vote/", PostVoteView.as_view(), name='post-vote-url'),

    path("post-vote/<int:post_vote_id>/", PostUpdateView.as_view(), name='post-vote-update-url'),
    
]