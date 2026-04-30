from django.forms import fields
from django import forms
from tasks.models import TaskModel

class TaskForm(forms.ModelForm):
  class Meta:
    model=TaskModel
    fields='__all__'
    exclude=['created_by']
    widgets={
      'due_date':forms.DateInput(attrs={
        'class':'form-control',
        'type':'date',
      })
    }
