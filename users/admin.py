from django.contrib import admin

from .models import User, RequestFreind


class RequestFreindsSendInline(admin.TabularInline):
    model = RequestFreind
    fk_name = 'from_user'
    extra = 3


class FreindsFromUserInline(admin.TabularInline):
    model = User.freinds.through
    fk_name = 'from_user'
    extra = 5


class FreindsToUserInline(admin.TabularInline):
    model = User.freinds.through
    fk_name = 'to_user'
    extra = 5


class UserAdmin(admin.ModelAdmin):
    inlines = [
        FreindsFromUserInline,
        FreindsToUserInline,
        RequestFreindsSendInline,
    ]
    exclude = ('freinds', )
    list_display = ('username', 'name', 'birthday', 'view_freinds')

    def view_freinds(self, obj):
        freinds = obj.freinds.all()
        if freinds:
            return list(freinds)
        return


class RequestFreindsAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'datetime_request', 'status')


admin.site.register(User, UserAdmin)
admin.site.register(RequestFreind, RequestFreindsAdmin)
