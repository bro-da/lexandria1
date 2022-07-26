


# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, category


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('category_name',)}
    list_display=('category_name','slug')

admin.site.register(Account, AccountAdmin)

admin.site.register(category,CategoryAdmin)