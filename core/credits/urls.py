
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


#from accounts.views import test
from credits.views.credits import InvitationsView, TransferView, WalletView

app_name = "credits-app"


urlpatterns = [
    
    path('invitations/', InvitationsView.as_view(), name="invitations-url"),
    path('transfer/', TransferView.as_view(), name="transfers-url"),
    path('wallet/<int:id>/', WalletView.as_view(), name='wallet-url'),
    
        
]
