from django import forms

class CommonLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'span2', 'placeholder':'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'span2', 'placeholder':'Password'}))