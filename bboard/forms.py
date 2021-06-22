from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title','content','price','rubric')
        