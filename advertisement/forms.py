from django import forms


from .models import Advertisement, BookMark


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ("title", "description", "image", "price", "category", "location")


class BookMarkForm(forms.ModelForm):
    class Meta:
        model = BookMark
        fields = []
