from django.views.generic import FormView, DetailView
from django.db.models import Q
from django_filters import FilterSet
from django_filters.views import FilterView

from .models import Advertisement, Category


class AdvertisementDetailView(DetailView):

    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'
    context_object_name = 'advertisement'

    
class AdvertisementListFilter(FilterSet):
    class Meta:
        model = Advertisement
        fields = {"title": ["contains"], "urgent": ["exact"]}

class AdvertisementCityListView(FilterView):
    context_object_name = "advertisements"
    template_name = 'advertisement/advertisement_list.html'
    filterset_class = AdvertisementListFilter
    paginate_by = 10
    
    
    def get_queryset(self):
        city = self.kwargs.get('city')
        if not city:
            city = self.request.COOKIES.get('selected_city')
        return Advertisement.objects.filter(location__city__slug=city)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["selected_city"] = self.kwargs.get('city') or self.request.COOKIES.get('selected_city')
        return context
    
        

# class AdvertisementCityCategoryListView(View):
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

class AdvertisementCityCategoryListView(AdvertisementCityListView):
    template_name = 'advertisement/advertisement_category_list.html'
    
    def get_queryset(self):
        city = self.kwargs.get('city')
        category = self.kwargs.get('category')
        return Advertisement.objects.filter(Q(location__city__slug=city) & Q(category__slug=category))
        

    

