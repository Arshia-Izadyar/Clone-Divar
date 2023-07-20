from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import UserAddressForm
from .models import UserAddress


User = get_user_model()


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "account/user_profile.html"
    model = User
    content_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not hasattr(self, "user_object"):
            self.user_object = User.objects.prefetch_related("bookmark", "advertisements").get(
                pk=self.request.user.pk
            )
       
        context["user"] = self.user_object
        context["bookmark"] = self.user_object.bookmark.all()
        context["advertisements"] = self.user_object.advertisements.all()

        return context

