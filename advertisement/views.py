from typing import Any
from django.views.generic import FormView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django_filters import FilterSet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from .models import Advertisement, Category, BookMark
from .forms import AdvertisementForm, BookMarkForm


class AdvertisementPostView(FormView):
    form_class = AdvertisementForm
    template_name = "advertisement/advertisement_post.html"
    success_url = "profile"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy(self.success_url))


class AdvertisementUpdateView(UpdateView):
    form_class = AdvertisementForm
    template_name = "advertisement/advertisement_update.html"
    model = Advertisement

    def get_queryset(self):
        return Advertisement.objects.filter(pk=self.kwargs.get("pk"))

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if Advertisement.is_belong_user(self.request.user, obj.pk):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404

    def get_success_url(self):
        selected_city = self.request.COOKIES.get("selected_city")
        if selected_city is not None:
            return reverse_lazy("adv-list", kwargs={"city": selected_city})
        else:
            return redirect("/")


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = "advertisement/advertisement_confirm_delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        selected_city = self.request.COOKIES.get("selected_city")
        if selected_city is not None:
            return reverse_lazy("adv-list", kwargs={"city": selected_city})
        else:
            return redirect("/")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if Advertisement.is_belong_user(self.request.user, obj.pk):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = self.get_object()
        context["selected_city"] = self.request.COOKIES.get("selected_city")
        return context


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = "advertisement/advertisement_detail.html"
    context_object_name = "advertisement"


class AdvertisementListFilter(FilterSet):
    class Meta:
        model = Advertisement
        fields = {"title": ["contains"], "urgent": ["exact"]}


class AdvertisementCityListView(FilterView):
    context_object_name = "advertisements"
    template_name = "advertisement/advertisement_list.html"
    filterset_class = AdvertisementListFilter
    paginate_by = 10

    def get_queryset(self):
        city = self.kwargs.get("city")
        return Advertisement.objects.filter(location__city__slug=city)

    def get_context_data(self, **kwargs):
        print(self.request.COOKIES)
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["selected_city"] = self.kwargs.get("city") or self.request.COOKIES.get("selected_city")
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        selected_city = self.kwargs.get("city") or self.request.COOKIES.get("selected_city")
        if selected_city:
            response.set_cookie("selected_city", selected_city, max_age=9000)
        return response


class AdvertisementCityCategoryListView(AdvertisementCityListView):
    template_name = "advertisement/advertisement_category_list.html"

    def get_queryset(self):
        city = self.kwargs.get("city")
        category = self.kwargs.get("category")
        return Advertisement.objects.filter(Q(location__city__slug=city) & Q(category__slug=category))


class AddToBookMark(DetailView):
    model = Advertisement

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = BookMarkForm(request.POST)
        obj = self.get_object()
        if form.is_valid():
            book_mark = form.save(commit=False)
            book_mark.user = request.user
            book_mark.advertisement = obj
            book_mark.save()
        return HttpResponseRedirect(obj.get_absolute_url())




class RemoveFromBookMark(DetailView):
    model = Advertisement

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        bookmark = get_object_or_404(BookMark, advertisement=obj, user=request.user)
        bookmark.delete()
        return HttpResponseRedirect(obj.get_absolute_url())
