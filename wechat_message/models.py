from django.utils.translation import ugettext_lazy as _
from django.db import models

class Message(models.Model):
    keyword = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword

    def __unicode__(self):
        return self.keyword

