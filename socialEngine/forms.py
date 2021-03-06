from django import forms
from socialApp.models import Profile

class ProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Repeat password')
    class Meta:
        model = Profile
        fields = ('email', 'firstName', 'lastName', 'birth_date', 'sex')
        
class PubForm(forms.ModelForm):
    pub_text = forms.CharField(label='Your wall post', max_length=400)


