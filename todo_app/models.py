from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_title = models.CharField(max_length=250, default='Add your TODO here', blank=False)
    todo_description = models.TextField(blank=True, default='Your todo description ')
    is_todo_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='media/profile_pic/%Y/%m/', blank=True, default='default.jpg')

    def __str__(self):
        return self.user.username



