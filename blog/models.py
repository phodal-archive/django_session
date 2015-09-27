# -*- coding: utf-8 -*-

from django.core import validators
from django.db import models
from django.utils.translation import ugettext as _
import re


class Blog(models.Model):
    title = models.CharField(_("title"), max_length=30, help_text="请输入标题")
    content = models.TextField("内容")
    author = models.CharField(max_length=30, validators=[
        validators.RegexValidator(re.compile('^\w$'),
                                  _('Please input valid author name'), 'invalid')
    ])
    date = models.DateTimeField(auto_now=True)
