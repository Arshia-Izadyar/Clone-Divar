from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from locations.models import Location
User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children")
    
class Advertisement(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='advertisements',)
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('description'))
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='advertisements', verbose_name=_('location')
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="advertisements", verbose_name=_('category')
    )
    image = models.ImageField(upload_to="images/", verbose_name=_("Image"))

    def __str__(self):
            return f"{self.title} > {self.location.city.name}"
        
        
    @classmethod
    def is_belong_user(cls, user, advertisement_pk):
        advertisement = cls.objects.get(pk=advertisement_pk)
        return user == advertisement.user