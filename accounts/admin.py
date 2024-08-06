from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, User


class UserAdmin(BaseUserAdmin):
    # Specify the fields to be used in displaying the User model.
    list_display = (
        'nationalCode',
        'email',
        'firstName',
        'lastName',
        'is_active',
        'is_staff',
        'is_verified',
        'last_login',
        'create_date',
    )

    # Specify the fields to be used when adding or editing the User model.
    fieldsets = (
        (None, {'fields': ('nationalCode', 'email', 'password')}),
        ('Personal info', {'fields': ('firstName', 'lastName', 'description', 'phone', 'mobile')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified')}),
        ('Important dates', {'fields': ('last_login', 'create_date', 'update_date')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nationalCode', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified')}
         ),
    )

    # Add filters and search fields
    list_filter = ('is_staff', 'is_active', 'is_verified')
    search_fields = ('nationalCode', 'email', 'firstName', 'lastName')
    ordering = ('create_date',)
    filter_horizontal = ()


# Register the CustomUser model with the UserAdmin
admin.site.register(CustomUser, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ['nationalCode', 'email', 'firstName', 'lastName',
                'phone',
                'mobile',
                ]

    def get_list_display(self, request):
        return ['nationalCode',
                'email',
                'firstName',
                'lastName',
                'phone',
                'mobile',
                'is_verified',
                'is_active',
                'is_staff',
                'last_login',
                ]

    def get_search_fields(self, request):
        return ['nationalCode',
                'email',
                'firstName',
                'lastName',
                'phone',
                'mobile',
                ]

    def get_list_filter(self, request, filters=None):
        return ['nationalCode',
                'email',
                'firstName',
                'lastName',
                'phone',
                'mobile',
                ]