from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from private_messages.views.private_messages import PrivateMessagesView, PrivateMesssagesDetailView

app_name = "messages-app"

urlpatterns = [
    path('private-messages-all/', PrivateMessagesView.as_view(), name='pm-all'),
    path('private-message/<int:id>/', PrivateMesssagesDetailView.as_view(), name='get-pm'),
       

]