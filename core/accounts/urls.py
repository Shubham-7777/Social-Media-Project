


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


#from accounts.views import test
from accounts.views.user import UserView


app_name = "accounts-app"

urlpatterns = [
    #path('', test, name="test_url"),
    
    path('users/', UserView.as_view(), name='user-url'),
    
]

