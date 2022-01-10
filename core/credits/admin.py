from django.contrib import admin
from credits.models.credits import Invitation, Transfer, Wallet


# Register your models here.
admin.site.register(Invitation)
admin.site.register(Transfer)
admin.site.register(Wallet)
