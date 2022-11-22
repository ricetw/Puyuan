from django.contrib import admin
from User.models import *
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'account', 'phone', 'email', 'password',
        'invite_code', 'verified', 'privacy_policy', 'must_change_password', 'name',
        'birthday', 'height', 'gender', 'fcm_id', 'address',
        'weight', 'fb_id', 'status', 'group', 'unread_records',
        'badge', 'login_times', 'created_at', 'updated_at',
    )


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'VerificationCode')


# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
    # list_display=('id','user_id','account','sessionkey')