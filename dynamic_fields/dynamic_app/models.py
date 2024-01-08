from django.db import models
# from django.utils import timezone

# # Create your models here. Generate dynamic fields using serialiazers

# class  Author(models.Model):
#     name=models.CharField(max_length=40)
#     dob=models.DateField(verbose_name='date of birth')
#     dynamic_fields = models.JSONField(default=dict)

#     # @property
#     # def age(self):
#     #     return timezone.now().year - self.dob.year

#     def add_dynamic_field(self, field_name, field_value):
#         self.dynamic_fields[field_name] = field_value
#         self.save()
    

# dynamic_models/base.py
from dynamic_models.factory import create_dynamic_model, register_dynamic_model

fields=[
    {'name':'field1','type':'CharField','params':{'max_length':50}},
    {'name':'field2','type':'IntegerField'},
]
DynamicModel = create_dynamic_model('DynamicModel', fields)
register_dynamic_model('dynamic_app', DynamicModel)



