from django import forms
class myadd_trainee_form(forms.Form):
    trainee_name = forms.CharField()
    trainee_email = forms.EmailField()
