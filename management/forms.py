from django import forms
from .models import Teacher, ClassRoom


class ClassroomForm(forms.Form):
    idTeacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), to_field_name='first_name')
    name = forms.CharField(max_length=2, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    sur_name = forms.CharField(max_length=200)
    born_date = forms.DateField()
    idClassroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all(), to_field_name='name')
    grade_lab = forms.FloatField(max_value=20)
    grade_exam = forms.FloatField(max_value=20)
    grade_final = forms.FloatField(max_value=20)