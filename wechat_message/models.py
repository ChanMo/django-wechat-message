from django.utils.translation import ugettext_lazy as _
from django.db import models

class Message(models.Model):
    keyword = models.CharField(_('keyword'), max_length=200, unique=True)
    content = models.TextField(_('content'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.keyword

    def __unicode__(self):
        return self.keyword

    class Meta(object):
        verbose_name = _('wechat message')
        verbose_name_plural = _('wechat message')
