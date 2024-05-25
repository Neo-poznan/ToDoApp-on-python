from django import forms


class CategoryCreationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'clean',
        'id': 'name-id-for-label' ,
    }))


    color = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'color',
        'class': 'color-picker',
        'value': '',
        }))