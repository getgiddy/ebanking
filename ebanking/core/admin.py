from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import (
    UserProfile,
    Account,
    Beneficiary,
    Transaction,
    Application,
)


class InlineUser(admin.StackedInline):
    model = get_user_model()


class InlineProfile(admin.StackedInline):
    model = UserProfile


class AccountAdmin(admin.ModelAdmin):
    inlines = [InlineProfile]
    

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (('Personal info'), {'fields': ('username', 'first_name', 'last_name', 'email', 'password')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ()


class InlineTransaction(admin.TabularInline):
    model = Transaction
    extra = 1


class BeneficiaryAdmin(admin.ModelAdmin):
    inlines = [InlineTransaction]

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Account, AccountAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Application)