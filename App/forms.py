
from django import forms
class uploadFilesForm(forms.form):
      rubric= forms.FileField(label = 'upload Rubric PDF')
      essay= forms.FileField(label='upload Essay PDF')