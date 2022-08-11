from django import forms
from .models import Query

class QueryForm(forms.ModelForm):

  # def clean_email(self):
  #   email = self.cleaned_data.get('email')
  #   if not '@' in email:
  #     raise forms.ValidationError('メールアドレスの形式で入力してください。')
  #   return email

  class Meta:
    model = Query
    fields = ['name', 'email', 'phone', 'text']
    widgets = {
      'name': forms.TextInput(
        attrs={'class': 'tm-input', 'placeholder': '※Name'}
      ),
      'email': forms.TextInput(
        attrs={'class': 'tm-input', 'placeholder': '※Email'}
      ),
      'phone': forms.TextInput(
        attrs={'class': 'tm-input', 'placeholder': 'Tel'}
      ),
      'text': forms.Textarea(
        attrs={
          'class': 'tm-input', 
          'placeholder': '※Text',
          'rows': 8
        }
      )
    }