from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Add(models.Model):
    foodName = models.CharField("음식이름", max_length=30)
    pic = models.ImageField("사진", default='media/default_image.jpeg')
    GPS = models.CharField("위치", max_length=300, blank=True)
    taste = models.TextField("음식평", max_length=300, blank=True)
    date = models.DateTimeField("작성한시간", auto_now_add=True)
    fix = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        self.date = timezone.now()
        self.save()
        return self.foodName


class LOGIN(models.Model):
    text = models.TextField()
