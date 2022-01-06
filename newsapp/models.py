from django.db import models

# Create your models here.
class newsdetails(models.Model):
    current_url = models.CharField(max_length=150)
    categories = models.CharField(max_length=150)
    sub_categories = models.CharField(max_length=150)
    headline = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    images = models.CharField(max_length=150)
    news_detail = models.CharField(max_length=150)