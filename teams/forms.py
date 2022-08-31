from django import forms

class NameForm(forms.Form):
    yourname = forms.CharField(label = 'Your Name', max_length=100)
