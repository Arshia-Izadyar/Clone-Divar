from django.urls import path

from .views import TransactionView

urlpatterns = [
    path("create/<int:package_id>/<int:adv_id>/", TransactionView.as_view(), name="transaction-create"),
]
