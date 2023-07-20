from django.shortcuts import render


from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import FormView, DetailView, ListView

from .models import Advertisement, Category


from django_filters import FilterSet
from django_filters.views import FilterView

# class PostAdvertisementView(FormView):
#     """ Get form from PostAdvertisementForm 📢"""

#     template_name = 'advertisement/post_advertisement.html'
#     form_class = PostAdvertisementForm
#     success_url = '/'

#     def form_valid(self, form):
#         # get user from request
#         user = self.request.user
#         form.cleaned_data['images'] = self.request.FILES.getlist('files')
#         form.save(user)
#         return super().form_valid(form)


class AdvertisementDetailView(DetailView):

    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'
    context_object_name = 'advertisement'
    
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Advertisement.objects.get(pk=1)

    
class AdvertisementCityListFilter(FilterSet):
    class Meta:
        model = Advertisement
        fields = {"title": ["contains"], "urgent": ["exact"]}

class AdvertisementCityListView(FilterView):
    context_object_name = "advertisements"
    template_name = 'advertisement/advertisement_list.html'
    filterset_class = AdvertisementCityListFilter
    paginate_by = 10
    
    
    def get_queryset(self):
        city = self.kwargs.get('city')
        return Advertisement.objects.filter(location__city__slug=city)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context
    
        
        
        
    

# class AdvertisementCityCategoryListView(View):
#     """
#     Get advertisement by cities 🏙 and categories 🔠 from Advertisement model
#     """

#     def get(self, request, *args, **kwargs):
#         city = self.kwargs.get('city')
#         category = self.kwargs.get('category')
#         queryset = Advertisement.objects.filter(location__city__slug=city, category__slug=category)
#         categories = Category.objects.all()
#         filter = AdvertisementFilter(self.request.GET, queryset=queryset)
#         return render(
#             request, 'advertisement/advertisement_list.html',
#             context={'filter': filter, 'categories': categories, 'city': city}
#         )

#     def post(self, request, *args, **kwargs):
#         form = self.request.AdvertisementFilter(self.request.GET)
#         if form.is_valid():
#             return render(request, 'advertisement/advertisement_list.html', context={'filter': form.qs})


# # A decorator that caches 🔂 the page for 3 minutes.
# @method_decorator(cache_page(60 * 3), name='dispatch')
# class AdvertisementTehranListView(AdvertisementCityListView):
#     """
#     This view inherited from AdvertisementCityListView to cache 🔂 Advertisements in "Tehran" City.
#     "Tehran" is capital of IRAN 🇮🇷 and it has so many request per seconds ⏳ . This is why we have to cache 🔂 this View
#     """

#     def get(self, request, *args, **kwargs):
#         self.kwargs['city'] = 'tehran'
#         return super().get(request, *args, **kwargs)