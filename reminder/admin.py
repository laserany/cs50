from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from reminder.models import CustomUser, Record, Group, GroupMember
from reminder.forms import RegisterForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                      
            'Phone number', 
            {
                'fields': (
                    'phone',
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Record)
admin.site.register(Group)
admin.site.register(GroupMember)
