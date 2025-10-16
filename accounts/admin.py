from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import User,UserProfile

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2'),
        }),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)