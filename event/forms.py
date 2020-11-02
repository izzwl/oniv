from django import forms
from .models import Attendance,CongratulationWhises

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'name','phone','email','is_attend','guest','whises',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name','class':'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone','type':'tel','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email','class':'form-control'}),
            'whises': forms.Textarea(attrs={'placeholder': 'Your Whises','class':'form-control'}),
            'is_attend': forms.RadioSelect(choices=((True,'i will attend'),(False,'no, i can\'t attend'))),
            'guest': forms.Select(choices=((1,'1 person'),(2,'2 Person'),(3,'3 Person'))),
        }

class CongratulationWhisesForm(forms.ModelForm):
    class Meta:
        model = CongratulationWhises
        fields = [
            'message',
        ]