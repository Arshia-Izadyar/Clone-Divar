from django.db import models
from django.utils.translation import gettext as _




class Province(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name=_('slug'))

    def __str__(self):
        return f"Province: {self.name}"

    class Meta:
        verbose_name = 'province'
        verbose_name_plural = 'provinces'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', unique=True, blank=True, verbose_name=_('slug'))
    province = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE, verbose_name=_('state'))


    def __str__(self):
        return f"City:{self.name} province: {self.province}"

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('advertisement-list', args=[self.name])

class District(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name=_('slug'))
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE, verbose_name=_('city'))

    def __str__(self):
        return f"{self.name} {self.city}"

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')


class Location(models.Model):
  
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name=_('province'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name=_('city'))
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('district'))

    def __str__(self):
        return f"{self.city} - {self.city}"

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _("locations")