from django import forms
from .models import Ad

# class AdForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ["title", "content"]