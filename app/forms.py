from django import forms
from .models import image

class image_form(forms.ModelForm):
    class Meta:
        model = image
        fields = "__all__"
        labels = {'photo':''}
        