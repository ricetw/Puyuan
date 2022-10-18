from django.db import models

# Create your models here.


class Friendsend(models.Model):

    user_id = models.CharField(max_length=20)
    relation_id = models.CharField(max_length=20)
    type = models.IntegerField()
    status = models.IntegerField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "id:{0}, user_id:{1}, relation_id:{2}, type:{3}, status:{4}, read:{5}, created_at:{6}, updated_at:{7}".format(
            self.pk, self.user_id, self.relation_id, self.type, self.status, self.read, self.created_at, self.updated_at
        )


class Share(models.Model):

    user_id = models.CharField(max_length=20, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    profile_id = models.IntegerField(null=True, blank=True)
    relation_type = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'id:{0}, user_id:{1}, type:{2}, profile_id:{3}, relation_type:{4}'.format(
            self.pk, self.user_id, self.type, self.profile_id, self.relation_type
        )
