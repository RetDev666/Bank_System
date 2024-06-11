from django.contrib import admin
from .models import CentralOffice, Branch, Client, Account

admin.site.register(CentralOffice)
admin.site.register(Branch)
admin.site.register(Client)
admin.site.register(Account)
