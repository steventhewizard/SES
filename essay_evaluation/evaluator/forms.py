from django import forms

class UploadForm(forms.Form):
    essay_file = forms.FileField()
    rubric_file = forms.FileField()
