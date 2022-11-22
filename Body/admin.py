from django.contrib import admin
from Body.models import *

# Register your models here.


@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'systolic',
                    'diastolic', 'pulse', 'recorded_at')


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'weight',
                    'body_fat', 'bmi', 'recorded_at')


@admin.register(BloodSugar)
class BloodSugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'sugar', 'exercise', 'drug',
                    'timeperiod', 'recorded_at')


@admin.register(UserDefault)
class UserDefaultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'sugar_delta_max', 'sugar_delta_min', 'sugar_morning_max', 'sugar_morning_min',
                    'sugar_evening_max', 'sugar_evening_min', 'sugar_before_max', 'sugar_before_min', 'sugar_after_max',
                    'sugar_after_min', 'systolic_max', 'systolic_min', 'diastolic_max', 'diastolic_min', 'pulse_max',
                    'pulse_min', 'weight_max', 'weight_min', 'bmi_max', 'bmi_min', 'body_fat_max', 'body_fat_min',
                    'created_at', 'updated_at'
                    )


@admin.register(UserSetting)
class UserSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'after_recording', 'no_recording_for_a_day', 'over_max_or_under_min',
                    'after_meal', 'unit_of_sugar', 'unit_of_weight', 'unit_of_height', 'created_at', 'updated_at')


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', "description", "meal", "tag",
                    "image", "lat", "lng", "recorded_at")


@admin.register(Medical)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'diabetes_type', 'oad',
                    'insulin', 'anti_hypertensives', 'created_at', 'updated_at')


@admin.register(Alc)
class AlcAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "a1c", "recorded_at",
                    "created_at", "updated_at")


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "type", "name", "recorded_at")


@admin.register(Care)
class CareAdmin(admin.ModelAdmin):
    list_display = 'id', 'user_id', 'member_id', 'reply_id', 'message', 'created_at', 'updated_at'
