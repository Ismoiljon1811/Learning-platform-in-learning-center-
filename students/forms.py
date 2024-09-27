from django import forms

class HomeworkFrom(forms.Form):
       dascription = forms.CharField(widget=forms.Textarea)
       homework_file = forms.FileField(widget=forms.FileInput)

class HomeworkGForm(forms.Form):
       dascription = forms.CharField(widget=forms.Textarea({"class": "form-control"}))
       homework_file = forms.FileField(widget=forms.FileInput({"class": "form-control"}))
       date = forms.DateField(widget=forms.DateTimeInput({"class": "form-control"}))
