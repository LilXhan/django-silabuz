from django import forms 
from .models import ClassRoom

class StudenForm(forms.Form):

    first_name = forms.CharField(max_length=200)
    sur_name = forms.CharField(max_length=200)
    born_date = forms.DateField()
    # password = forms.PasswordInput()
    idClassroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all(), to_field_name='start_time')
    grade_lab =  forms.FloatField(max_value=20)
    grade_exam = forms.FloatField(max_value=20)
    grade_final = forms.FloatField(max_value=20)
