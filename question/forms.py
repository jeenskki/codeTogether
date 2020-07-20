from django import forms
from .models import Board, AttFile

class MyBoardForm(forms.ModelForm):
  class Meta:
    model = Board
    fields = '__all__'


class MyAttFileForm(forms.ModelForm):
  image = forms.ImageField(required=False)

  class Meta:
    model = AttFile
    exclude = ('board',)