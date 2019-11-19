from django import forms
from adminbackend.models import HomeContactForm
from datetime import datetime


class HomeForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    date = forms.DateField(initial=datetime.now().strftime("%Y-%m-%d"))
    email = forms.EmailField()
    time = forms.TimeField(initial=datetime.now().strftime("%H:%M:%S"))
    phone = forms.IntegerField()
    people = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':15}))
    error_css_class = 'error'
    required_css_class = 'bold'

    class Meta:
        model = HomeContactForm
        fields = ('name','date','email','time','phone','people','message',)
