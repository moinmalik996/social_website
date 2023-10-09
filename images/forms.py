from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image

import requests

class ImageForm(forms.Model):

    class Meta:
        model = Image
        fields = ['title', 'description', 'url']
        widgets = {
            'url': forms.HiddenInput
        }


    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given image have no valid extension.')
        return url

    def save(self, forece_insert=False, force_update=False, commit=True):
        image_obj = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image_obj.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f"{name}.{extension}"

        #downlaof image from the given URL
        response = requests.get(image_url)
        image_obj.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image_obj.save()
        
        return image_obj