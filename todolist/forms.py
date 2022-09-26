from django import forms

class ToDoListForms(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.TextInput)