from django import forms


class French(forms.Form):
    string = forms.CharField(label='string', max_length=100)