from django.contrib import admin
from Friend.models import *
# Register your models here.


@admin.register(Friendsend)
class FriendsendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'relation_id', 'type',
                    'status', 'read', 'created_at', 'updated_at')


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'type', 'profile_id', 'relation_type')
