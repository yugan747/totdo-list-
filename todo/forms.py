from django import forms
from .models import Todolist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class takelist(forms.ModelForm):
    class Meta:
        model=Todolist
        fields=['Descriptions','Remainder']

        widgets={
            'Descriptions':forms.Textarea(attrs={'class':'form-control'}),
            'Remainder':forms.SelectDateWidget()
        }

class usercreation(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','email','password1','password2']        