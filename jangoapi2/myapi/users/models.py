from django.db import models
class Users(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=10)
    usermobile = models.CharField(max_length=15)
    addres=models.TextField()
    def __str__(self):
        return self.userid
