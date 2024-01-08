# dynamic_models/fields.py
from django.db import models
from .base import DynamicModelBase

class DynamicCharField(DynamicModelBase):
    name = models.CharField(max_length=255)

class DynamicDateField(DynamicModelBase):
    name = models.DateField()
