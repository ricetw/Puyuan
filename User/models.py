from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):

    account = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=False)
    password = models.CharField(max_length=20, unique=False)

    invite_code = models.CharField(max_length=6, unique=True)

    verified = models.BooleanField(default=False, unique=False)
    privacy_policy = models.BooleanField(default=False, unique=False)
    must_change_password = models.BooleanField(default=False, unique=False)

    name = models.CharField(max_length=20, null=True, blank=True, unique=False)
    birthday = models.DateField(null=True, blank=True, unique=False)
    height = models.IntegerField(null=True, blank=True, unique=False)
    gender = models.IntegerField(default=False, unique=False)
    fcm_id = models.CharField(max_length=20, null=True,
                              blank=True, unique=False)
    address = models.CharField(
        max_length=150, null=True, blank=True, unique=False)
    weight = models.FloatField(null=True, blank=True, unique=False)

    fb_id = models.CharField(max_length=20, null=True,
                             blank=True, unique=False)
    status = models.CharField(max_length=20, null=True,
                              blank=True, unique=False)
    group = models.CharField(max_length=20, null=True,
                             blank=True, unique=False)
    unread_records = models.IntegerField(null=True, blank=True, unique=False)
    badge = models.CharField(max_length=20, null=True,
                             blank=True, unique=False)
    login_times = models.IntegerField(null=True, blank=True, unique=False)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, unique=False)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=True, unique=False)

    def __str__(self):
        return 'id:{0}, account:{1}, phone:{2}, email:{3}, password:{4}, invite_code:{5}, verified:{6}, privacy_policy:{7}, must_change_password:{8}, name:{9}, birthday:{10}, height:{11}, gender:{12}, fcm_id:{13}, address:{14}, weight:{15}, fb_id:{16}, status:{17}, group:{18}, unread_records:{19}, badge:{20}, login_times:{21}, created_at:{22}, updated_at:{23}'.format(
            self.pk, self.account, self.phone, self.email, self.password,
            self.invite_code, self.verified, self.privacy_policy, self.must_change_password, self.name,
            self.birthday, self.height, self.gender, self.fcm_id, self.address,
            self.weight, self.fb_id, self.status, self.group, self.unread_records,
            self.badge, self.login_times, self.created_at, self.updated_at
        )


class VerificationCode(models.Model):
    email = models.EmailField(max_length=100)
    VerificationCode = models.CharField(max_length=6)

    def __str__(self):
        return 'id:{2}, email:{0} ,VerificationCode:{1}'.format(
            self.email, self.VerificationCode, self.pk)
