from django.contrib import admin
from account.models import Info, UserToken


@admin.register(Info)
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'telphone', 'create_date', 'update_date')


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('username', 'token')
