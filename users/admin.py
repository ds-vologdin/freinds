from django.contrib import admin

from .models import User, RequestFriend


class RequestfriendsSendInline(admin.TabularInline):
    model = RequestFriend
    fk_name = 'from_user'
    extra = 3


class friendsFromUserInline(admin.TabularInline):
    model = User.friends.through
    fk_name = 'from_user'
    extra = 5


class friendsToUserInline(admin.TabularInline):
    model = User.friends.through
    fk_name = 'to_user'
    extra = 5


class UserAdmin(admin.ModelAdmin):
    inlines = [
        friendsFromUserInline,
        friendsToUserInline,
        RequestfriendsSendInline,
    ]
    exclude = ('friends', )
    list_display = ('username', 'name', 'birthday', 'view_friends')

    def view_friends(self, obj):
        friends = obj.friends.all()
        if friends:
            return list(friends)
        return


class RequestfriendsAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'datetime_request', 'status')


admin.site.register(User, UserAdmin)
admin.site.register(RequestFriend, RequestfriendsAdmin)
