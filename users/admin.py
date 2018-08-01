from django.contrib import admin

from .models import User


class FreindsFromUserInline(admin.TabularInline):
    model = User.freinds.through
    fk_name = 'from_user'
    extra = 5


class FreindsToUserInline(admin.TabularInline):
    model = User.freinds.through
    fk_name = 'to_user'
    extra = 5


class UserAdmin(admin.ModelAdmin):
    inlines = [FreindsFromUserInline, FreindsToUserInline]
    exclude = ('freinds', )
    list_display = ('username', 'name', 'birthday', 'get_all_freinds')


admin.site.register(User, UserAdmin)
