from django.contrib import admin
#from accounts.models.profile import Profile
from accounts.models.user import UserProfile


admin.site.register(UserProfile)
