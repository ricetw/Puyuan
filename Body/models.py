from django.db import models
import ast

# Create your models here.


class ListField(models.TextField):

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class BloodPressure(models.Model):

    user_id = models.CharField(max_length=20)
    systolic = models.FloatField(null=True, blank=True)
    diastolic = models.FloatField(null=True, blank=True)
    pulse = models.CharField(max_length=20, null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '"id":{0}, "user_id":{1}, "systolic":{2}, "diastolic":{3}, "pulse":{4}, "recorded_at":{5}'.format(
            self.pk,  self.user_id, self.systolic, self.diastolic, self.pulse, self.recorded_at)


class Weight(models.Model):

    user_id = models.CharField(max_length=20)
    weight = models.FloatField(null=True, blank=True)
    body_fat = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '"id":{0}, "user_id":{1}, "weight":{2}, "body_fat":{3}, "bmi":{4}, "recorded_at":{5}'.format(
            self.pk,  self.user_id, self.weight, self.body_fat, self.bmi, self.recorded_at)


class BloodSugar(models.Model):

    user_id = models.CharField(max_length=20)
    sugar = models.FloatField(null=True, blank=True)
    exercise = models.FloatField(null=True, blank=True)
    drug = models.FloatField(null=True, blank=True)
    timeperiod = models.IntegerField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '"id":{0}, "user_id":{1}, "sugar":{2}, "exercise":{3}, "drug":{4}, "timeperiod":{5}, "recorded_at":{6}'.format(
            self.pk,  self.user_id, self.sugar, self.exercise, self.drug, self.timeperiod, self.recorded_at)


class UserDefault(models.Model):
    user_id = models.CharField(max_length=20)
    sugar_delta_max = models.IntegerField(null=True, blank=True)
    sugar_delta_min = models.IntegerField(null=True, blank=True)
    sugar_morning_max = models.IntegerField(null=True, blank=True)
    sugar_morning_min = models.IntegerField(null=True, blank=True)
    sugar_evening_max = models.IntegerField(null=True, blank=True)
    sugar_evening_min = models.IntegerField(null=True, blank=True)
    sugar_before_max = models.IntegerField(null=True, blank=True)
    sugar_before_min = models.IntegerField(null=True, blank=True)
    sugar_after_max = models.IntegerField(null=True, blank=True)
    sugar_after_min = models.IntegerField(null=True, blank=True)
    systolic_max = models.IntegerField(null=True, blank=True)
    systolic_min = models.IntegerField(null=True, blank=True)
    diastolic_max = models.IntegerField(null=True, blank=True)
    diastolic_min = models.IntegerField(null=True, blank=True)
    pulse_max = models.IntegerField(null=True, blank=True)
    pulse_min = models.IntegerField(null=True, blank=True)
    weight_max = models.IntegerField(null=True, blank=True)
    weight_min = models.IntegerField(null=True, blank=True)
    bmi_max = models.IntegerField(null=True, blank=True)
    bmi_min = models.IntegerField(null=True, blank=True)
    body_fat_max = models.IntegerField(null=True, blank=True)
    body_fat_min = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, unique=False)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=True, unique=False)

    class Meta:
        db_table = "Userdefault"

    def __str__(self):
        return 'id：{0}, user_id：{1}, sugar_delta_max：{2}, sugar_delta_min：{3}, sugar_morning_max：{4}, sugar_morning_min：{5},sugar_evening_max：{6}, sugar_evening_min：{7}, sugar_before_max：{8}, sugar_before_min：{9}, sugar_after_max：{10},sugar_after_min：{11}, systolic_max：{12}, systolic_min：{13}, diastolic_max：{14}, diastolic_min：{15}, pulse_max：{16},pulse_min：{17}, weight_max：{18}, weight_min：{19}, bmi_max：{20}, bmi_min：{21}, body_fat_max：{22}, body_fat_min：{23},created_at:{24},updated_at:{25}'.format(
            self.pk, self.user_id, self.sugar_delta_max, self.sugar_delta_min, self.sugar_morning_max, self.sugar_morning_min,
            self.sugar_evening_max, self.sugar_evening_min, self.sugar_before_max, self.sugar_before_min, self.sugar_after_max,
            self.sugar_after_min, self.systolic_max, self.systolic_min, self.diastolic_max, self.diastolic_min, self.pulse_max,
            self.pulse_min, self.weight_max, self.weight_min, self.bmi_max, self.bmi_min, self.body_fat_max, self.body_fat_min,
            self.created_at, self.updated_at)


class UserSetting(models.Model):
    user_id = models.CharField(max_length=20)
    after_recording = models.BooleanField(
        default=False, null=True, blank=True)
    no_recording_for_a_day = models.BooleanField(
        default=False, null=True, blank=True)
    over_max_or_under_min = models.BooleanField(
        default=False, null=True, blank=True)
    after_meal = models.BooleanField(
        default=False, null=True, blank=True)
    unit_of_sugar = models.BooleanField(
        default=False, null=True, blank=True)
    unit_of_weight = models.BooleanField(
        default=False, null=True, blank=True)
    unit_of_height = models.BooleanField(
        default=False, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, unique=False)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=True, unique=False)

    class Meta:
        db_table = "Usersetting"

    def __str__(self):
        return 'id: {0}, user_id：{1}, after_recording: {2}, no_recording_for_a_day: {3}, over_max_or_under_min: {4}, after_meal: {5}, unit_of_sugar: {6}, unit_of_weight: {7}, unit_of_height: {8}, created_at: {9}, updated_at: {10}' .format(
            self.pk, self.user_id, self.after_recording, self.no_recording_for_a_day, self.over_max_or_under_min,
            self.after_meal, self.unit_of_sugar, self.unit_of_weight, self.unit_of_height, self.created_at, self.updated_at
        )


class Diet(models.Model):

    user_id = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True, blank=True)
    meal = models.IntegerField(null=True, blank=True)
    tag = ListField(max_length=200, null=True, blank=True)
    image = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '"id":{0}, "user_id":{1}, "description":{2}, "meal":{3}, "tag":{4}, "image":{5}, "lat":{6}, "lng":{7}, "recorded_at":{8}'.format(
            self.pk,  self.user_id, self.description, self.meal, self.tag, self.image, self.lat, self.lng, self.recorded_at)


class Medical(models.Model):
    user_id = models.CharField(max_length=20)
    diabetes_type = models.IntegerField(null=True, blank=True)
    oad = models.BooleanField(default=False, null=True, blank=True)
    insulin = models.BooleanField(default=False, null=True, blank=True)
    anti_hypertensives = models.BooleanField(
        default=False, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, unique=False)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=True, unique=False)

    def __str__(self):
        return 'id: {0}, user_id：{1}, diabetes_type: {2}, oad: {3}, insulin: {4}, anti_hypertensives: {5}, created_at: {6}, updated_at: {7}' .format(
            self.id, self.user_id, self.diabetes_type, self.oad, self.insulin,
            self.anti_hypertensives, self.created_at, self.updated_at
        )


class Alc(models.Model):
    user_id = models.CharField(max_length=20)
    a1c = models.CharField(max_length=20, null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, unique=False)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=True, unique=False)

    def __str__(self):
        return 'id: {0}, user_id：{1}, a1c: {2}, recorded_at: {3}, created_at: {4}, updated_at: {5}' .format(
            self.id, self.user_id, self.a1c, self.recorded_at, self.created_at, self.updated_at
        )


class Drug(models.Model):
    user_id = models.CharField(max_length=20)
    type = models.BooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'id:{0}, user_id:{1}, type:{2}, name:{3}, recorded_at:{4}'.format(
            self.pk, self.user_id, self.type, self.name, self.recorded_at
        )


class Care(models.Model):

    user_id = models.CharField(max_length=20, null=True, blank=True)
    member_id = models.CharField(max_length=20, null=True, blank=True)
    reply_id = models.CharField(max_length=20, null=True, blank=True)
    message = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'id:{0}, user_id:{1}, member_id:{2}, reply_id:{3}, message:{4}, created_at:{5}, updated_at:{6}'.format(
            self.pk, self.user_id, self.member_id, self.reply_id, self.message, self.created_at, self.updated_at
        )
