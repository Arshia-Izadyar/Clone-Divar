from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "account/user_profile.html"
    model = User
    content_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not hasattr(self, "user_object"):
            self.user_object = User.objects.prefetch_related("bookmarks", "advertisements").get(pk=self.request.user.pk)

        context["user"] = self.user_object
        context["bookmarks"] = self.user_object.bookmarks.all()
        context["advertisements"] = self.user_object.advertisements.all()

        return context
