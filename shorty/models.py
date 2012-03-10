from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from shorty.admins import UrlAdmin

class Url(models.Model):
    STATUS = (
        ('a','Active'),
        ('b','Banned'),
        ('p','Pending'),
        ('r','Refused')
    )
    user = models.ForeignKey(User,blank=True,null=True)
    url_field = models.URLField()
    personal_slug = models.CharField(max_length=125,blank=True,null=True)
    status = models.CharField(max_length=2)
    private = models.BooleanField(default=False)
    private_password = models.CharField(max_length=25,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    @property
    def is_active(self):
        if self.status == 'a':
            return True
        return None

    @property
    def is_banned(self):
        if self.status == 'b':
            return True
        return None

    @property
    def is_pending(self):
        if self.status == 'p':
            return True
        return None

    @property
    def is_refused(self):
        if self.status == 'r':
            return True
        return None
    
admin.site.register(Url,UrlAdmin)