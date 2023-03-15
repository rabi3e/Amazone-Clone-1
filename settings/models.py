from django.db import models
from django.utils.translation import gettext as _





# Create your models here.
class DeliveryFee(models.Model):
    fees = models.FloatField(_("Frais"))

    def __str__(self):
        return str(self.fees)

    class Meta:

        verbose_name = 'DeliveryFee'
        verbose_name_plural = 'DeliveryFees'