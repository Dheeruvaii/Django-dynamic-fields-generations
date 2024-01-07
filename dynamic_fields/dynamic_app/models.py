from django.db import models
from django.utils import timezone

# Create your models here. Generate dynamic fields using serialiazers

class  Author(models.Model):
    name=models.CharField(max_length=40)
    dob=models.DateField(verbose_name='date of birth')

    @property
    def age(self):
        return timezone.now().year - self.dob.year


    






