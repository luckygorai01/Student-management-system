from django import forms
from .models import addcourse

class addcourseForm(forms.ModelForm):
    class Meta:
        model = addcourse
        fields = ['student', 'course', 'section']
        
from .models import Marks

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']