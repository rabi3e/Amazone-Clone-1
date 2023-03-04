from django.db import models
from django.utils.translation import gettext as _
from product.models import Product
from django.contrib.auth.models import User


# Create your models here.
ORDER_STATUS = (
    ('R', 'Reçue'),
    ('T', 'Traitée'),
    ('E', 'Expédiée'),
    ('L', 'Livrée'),
)


class Order(models.Model):
    user= models.ForeignKey("User", verbose_name=_("Client"), on_delete=models.SET_NULL,null=True,blank=True)
    code = models.CharField(_("Code"), max_length=50)
    status = models.CharField(_("Status"), max_length=1, choices=ORDER_STATUS)
    order_time = models.DateTimeField(_("Heure de Commande"), auto_now=True)
    delivery_time = models.DateTimeField(_("Heure d'expédition"), auto_now=False, auto_now_add=False,null=True,blank=True)


    def __str__(self):
        self.code

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    

class OrderDetail(models.Model):
    ordre= models.ForeignKey("Order", verbose_name=_("Commande"), on_delete=models.CASCADE)
    product = models.ForeignKey("Product", verbose_name=_("Produit"), on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(_("Quantite"))
    price =models.FloatField(_("Prix"))
     

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails' 