from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
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


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'status', 'email', 'phone', 'country')
    list_filter = ('status', 'gender', 'account_type')
    search_fields = ('firstname', 'lastname', 'email', 'username', 'country')
    actions = ['approve']

    def full_name(self, obj):
        return f'{obj.firstname} {obj.lastname}'

    def approve(self, request, queryset):
        for obj in queryset:
            user = User.objects.create_user(
                username = obj.username,
                first_name = obj.firstname,
                last_name = obj.lastname,
                email = obj.email,
                password = obj.password,
            )

            user.save()

            account = Account.objects.create(
                user = user,
                account_name = obj.account_name,
                account_type = obj.account_type,
            )

            account.save()

            profile = UserProfile.objects.create(
                account = account,
                phone = obj.phone,
                date_of_birth = obj.date_of_birth,
                address = obj.address,
                country = obj.country,
                state = obj.state,
                city = obj.city,
                marital_status = obj.marital_status,
                gender = obj.gender,
                pin = obj.pin,
                image = obj.image,
            )

            profile.save()

        queryset.update(status='A')
            
    approve.short_description = 'Approve selected applications'


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Account, AccountAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Application, ApplicationAdmin)