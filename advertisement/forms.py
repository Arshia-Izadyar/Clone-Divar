from django import forms


from .models import Advertisement



class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ("title", "description", "image", "price", "category","location")