# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	""" Additive data about users - enlarging default User model"""
	account = models.OneToOneField(User, related_name='profile')
	cash = models.FloatField(default=0.0)
	user_type = models.PositiveSmallIntegerField(default=0) # 0 - customer, 1 - executor

class Task(models.Model):
	""" Describes tasks for executors from customers"""
	author = models.ForeignKey(User, related_name = 'task_author')
	executor = models.ForeignKey(User, related_name = 'task_executor', blank=True, null=True)
	title = models.CharField(max_length=140)
	description = models.TextField()
	posting_date = models.DateField(auto_now_add=True, blank=True)
	status = models.CharField(default='Открыта', max_length=15)
	cost = models.FloatField()

