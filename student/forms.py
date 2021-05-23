from django import forms

class studReg(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'attrib'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'attrib'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'attrib'}))