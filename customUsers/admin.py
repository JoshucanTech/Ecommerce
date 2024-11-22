from django.contrib import admin
from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin


admin.site.register(CustomUser)




# # Custom User Admin class for the CustomUser model
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'is_staff', 'is_superuser')
#     list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_of_birth')  # Filters for the admin list view
#     search_fields = ('email', 'username', 'first_name', 'last_name')  # Add search functionality
#     ordering = ('email',)  # Default ordering
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {'fields': ('email', 'username', 'password1', 'password2')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )
#     filter_horizontal = ()  # Use this for many-to-many fields, e.g., for groups or user permissions
#     readonly_fields = ('last_login', 'date_joined')  # Read-only fields in the admin panel

# # Register your CustomUser model with the custom admin interface
# admin.site.register(CustomUser, CustomUserAdmin)
