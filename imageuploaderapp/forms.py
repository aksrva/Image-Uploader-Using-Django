from django import forms
from imageuploaderapp.models import ImageUploader


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUploader
        fields = "__all__"
        labels = {'image': ''}
