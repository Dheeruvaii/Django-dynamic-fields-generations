# dynamic_models/base.py
from django.db import models

class DynamicModelBase(models.Model):
    # Common fields and methods go here
    pass

    class Meta:
        abstract = True
