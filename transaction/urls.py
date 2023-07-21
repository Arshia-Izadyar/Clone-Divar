from django.urls import path

from .views import TransactionView, PaymentGateWay

urlpatterns = [
    path("create/<int:package_id>/<int:adv_id>/", TransactionView.as_view(), name="transaction-create"),
    path("confirm/<slug:invoice_id>/", PaymentGateWay.as_view(), name="transaction-confirm"),
]
