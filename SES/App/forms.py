from django import forms
from .models import Rubric, Essay
class uploadFilesForm(forms.form):
      rubric= forms.FileField(label = 'upload Rubric PDF')
      essay= forms.FileField(label='upload Essay PDF')
class RubricForm(forms.ModelForm):
    class Meta:
        model = Rubric
        fields = ['rubric_file']

class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        fields = ['essay_file']