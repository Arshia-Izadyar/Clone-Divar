from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .models import Transaction
from package.models import Package
from advertisement.models import Advertisement


class TransactionView(LoginRequiredMixin, View):
    template_name = "transaction/create_transaction.html"

    def get(self, request, package_id, adv_id, *args, **kwargs):
        if Advertisement.is_belong_user(request.user, adv_id):
            package = Package.objects.get(pk=package_id)

            t = Transaction.objects.create(
                user=request.user,
                package=package,
                amount=package.price,
                type=Transaction.PURCHASE,
                status=Transaction.PENDING,
            )
            return render(request, self.template_name, {"transaction": t, "package": package})
        else:
            raise Http404


class PaymentGateWay(LoginRequiredMixin, View):
    # i know we should use an abstraction level between low-level features and high-level features
    # but this is not the case for now
    # this isn't a real payment gate way ( i don't have one ) (its hard to get and zarinpaal sandbox is not working. i tried to)
    template_name = "transaction/confirm_transaction.html"

    def post(self, request, invoice_id, *args, **kwargs):
        t = Transaction.objects.get(invoice_number=invoice_id)
        if request.user == t.user:
            t.status = Transaction.PAID
            t.save()
            return render(request, self.template_name, {"transaction": t})
        else:
            raise Http404
