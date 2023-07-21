from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

import uuid

from package.models import Package

User = get_user_model()


class Transaction(models.Model):
    PAID = 10
    PENDING = 0
    NOT_PAID = -10

    transaction_status = ((PAID, _("paid")), (PENDING, _("pending")), (NOT_PAID, _("Not paid")))

    CHARGE = 1
    PURCHASE = 2

    transaction_type = ((PURCHASE, _("Purchase")), (CHARGE, _("Charge")))

    user = models.ForeignKey(
        User, verbose_name=_("User"), related_name="transactions", on_delete=models.SET("deleted_user")
    )
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=11, decimal_places=2)
    type = models.PositiveSmallIntegerField(verbose_name=_("Type"), choices=transaction_type, default=PURCHASE)
    status = models.SmallIntegerField(verbose_name=_("Status"), choices=transaction_status, default=NOT_PAID)
    created_date = models.DateTimeField(_("Created Date"), auto_now_add=True)
    invoice_number = models.UUIDField(_("Invoice number"), max_length=140, default=uuid.uuid4)
    package = models.ForeignKey(
        Package, verbose_name=_("Package"), related_name="transactions", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username} > {self.status} > {self.amount}"
