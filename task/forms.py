from django import forms
from . import models

class TaskForm(forms.ModelForm):
    
    class Meta:
        model  = models.Task
        exclude = ['user','user_point','task_completed_at','is_completed','is_late']
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'due_time':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
        }
        