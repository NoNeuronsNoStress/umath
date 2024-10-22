from django import forms


class InputUpperLimit(forms.Form):
    upper_limit = forms.CharField(label="",max_length=25, widget=forms.TextInput(attrs={
        'style': 'text-align: center; margin: 0 auto; display: block; position: absolute; top: 47%; left: 50%; transform: translate(-50%, -50%);',
        'class': 'input-upper-limit'
    }))
