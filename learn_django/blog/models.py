from django.db import models

# Create your models here.
class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    reporter = models.CharField(max_length=200, blank=False, null=False)
