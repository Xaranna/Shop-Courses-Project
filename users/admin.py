from django.contrib import admin
from shop.admin import CartAdmin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    inlines = (CartAdmin,)


# Register your models here.
admin.site.register(User, UserAdmin)