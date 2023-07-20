from typing import Any
from django.views.generic import FormView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django_filters import FilterSet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django_filters.views import FilterView
from django.urls import reverse_lazy

from .models import Advertisement, Category
from .forms import AdvertisementForm


class AdvertisementPostView(FormView):
    form_class = AdvertisementForm
    template_name = 'advertisement/advertisement_post.html'
    success_url = "profile"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy(self.success_url))
    

class AdvertisementUpdateView(UpdateView):
    form_class = AdvertisementForm
    template_name   = 'advertisement/advertisement_update.html'
    model = Advertisement
    
    def get_queryset(self):
        return Advertisement.objects.filter(pk=self.kwargs.get('pk'))
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404
    
    def get_success_url(self):
        selected_city = self.request.COOKIES.get('selected_city')
        if selected_city is not None:
        
            return reverse_lazy('adv-list', kwargs={'city': selected_city})
        else:
            return redirect('/')
    


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'advertisement/advertisement_confirm_delete.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        selected_city = self.request.COOKIES.get('selected_city')
        if selected_city is not None:
        
            return reverse_lazy('adv-list', kwargs={'city': selected_city})
        else:
            return redirect('/')


    def dispatch(self, request, *args, **kwargs):
        # Check if the user is the owner of the advertisement
        obj = self.get_object()
        if obj.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            # Redirect to some other page or show an error message
            return redirect('/')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = self.get_object()
        context["selected_city"] = self.request.COOKIES.get('selected_city')
        return context
    

    

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
        return Advertisement.objects.filter(location__city__slug=city)
    
    def get_context_data(self, **kwargs):
        print(self.request.COOKIES)
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["selected_city"] = self.kwargs.get('city') or self.request.COOKIES.get('selected_city')
        return context
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        selected_city = self.kwargs.get('city') or self.request.COOKIES.get('selected_city')
        if selected_city:
            # Set the city value to a cookie with an expiration time (e.g., 1 year)
            response.set_cookie('selected_city', selected_city, max_age=7000)  
        return response
    
        

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
        

    

