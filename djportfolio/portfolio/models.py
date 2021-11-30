from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
import datetime


class Project(models.Model):

    title = CharField(max_length=100)

    description = models.TextField()

    image = ImageField(upload_to="portfolio/images")

    url = URLField(blank=True)

    date = models.DateField(datetime.date.today)
    
