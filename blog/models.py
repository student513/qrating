# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase

PRICE = [(i,i*500+500) for i in range(10)]
DICT_PRICE = dict(PRICE)

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length = 40)
    content = models.TextField()
    time_created = models.DateTimeField()
    price = models.IntegerField(choices=PRICE)
    selected = models.BooleanField(default=False)

    tags = models.ManyToManyField('Tag', blank  = True)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    content = models.TextField()
    time_created = models.DateTimeField()
    selected = models.BooleanField(default=False)

class QuestionImage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file = ProcessedImageField(
        upload_to = 'images/',
        processors = [ResizeToFill(600,600)],
        format = 'JPEG',
        #option = {'quality':90},
    )

class AnswerImage(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    file = ProcessedImageField(
        upload_to = 'images/',
        processors = [ResizeToFill(600,600)],
        format = 'JPEG',
        #option = {'quality':90},
    )

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    num = models.IntegerField(default=0)