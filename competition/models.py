from django.db import models
from user.models import User
from autoslug import AutoSlugField


class Competition(models.Model):
    title = models.CharField( max_length=200,blank=True, null=True)
    slug = AutoSlugField(populate_from='title',blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    max_entry = models.IntegerField(blank=True, null=True)
    rules = models.TextField(blank=True, null=True)
    reg_fee = models.IntegerField(default=0)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.FileField(blank=True, null=True)
    category = models.CharField(max_length=100)
    locality = models.CharField(max_length=100, default="General")
    prize = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.title