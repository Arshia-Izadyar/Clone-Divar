from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from advertisement.models import Advertisement
from package.models import Package


class PackageView(LoginRequiredMixin, View):
    template_name = "package/package_advertisement.html"

    def get(self, request, package_pk, advertisement_pk):
        if not Advertisement.is_belong_user(request.user, advertisement_pk):
            raise Http404
        package = Package.objects.get(pk=package_pk)
        advertisement = Advertisement.objects.get(pk=advertisement_pk)
        return render(request, self.template_name, {"package": package, "advertisement": advertisement})


class PackageListView(LoginRequiredMixin, ListView):
    template_name = "package/package_list.html"
    queryset = Package.objects.all()
    context_object_name = "packages"

    def get_context_data(self, **kwargs):
        context = super(PackageListView, self).get_context_data(**kwargs)
        context["user"] = self.request.user
        context["advertisement_pk"] = self.kwargs["advertisement_pk"]
        return context
