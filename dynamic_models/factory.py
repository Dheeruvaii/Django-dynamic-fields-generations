# dynamic_models/factory.py
from django.apps import apps
from django.db import models
from .base import DynamicModelBase

def create_dynamic_model(model_name, fields):
    class Meta:
        verbose_name = model_name

    attrs = {'__module__': 'dynamic_models', 'Meta': Meta}
    for field in fields:
        attrs[field['name']] = getattr(models, field['type'])(**field.get('params', {}))

    model = type(model_name, (DynamicModelBase,), attrs)
    return model

def register_dynamic_model(app_name, model):
    apps.get_app_config(app_name).models_module.add_to_class(model.__name__, model)
