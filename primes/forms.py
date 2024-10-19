from django import forms


class InputUpperLimit(forms.Form): 
    upper_limit = forms.CharField(label="limit", max_length=25)

