from django.db import models
from django.utils.translation import gettext as _
from product.models import Product
from django.contrib.auth.models import User
from utils.generateur import generate_code





# Create Cart models
CART_STATUS = (
    ('E', 'En cours'),
    ('V', 'Validé'),

)


class Cart(models.Model):
    user= models.ForeignKey(User, verbose_name=_("Client"), related_name='user_cart' ,on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(_("Status"), max_length=1, choices=CART_STATUS)
    

    def __str__(self):
        return str(self.code)
        
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Casts'
    

class CartDetail(models.Model):
    cart= models.ForeignKey(Cart, verbose_name=_("Commande"), related_name='cart_details' ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Produit"), related_name='cart_product',on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(_("Quantite"))
    price =models.FloatField(_("Prix"))
    total = models.FloatField(_("Total"))
     

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'CartDetail'
        verbose_name_plural = 'CartDetails' 
# Create Order models
ORDER_STATUS = (
    ('R', 'Reçue'),
    ('T', 'Traitée'),
    ('E', 'Expédiée'),
    ('L', 'Livrée'),
)


class Order(models.Model):
    user= models.ForeignKey(User, verbose_name=_("Client"),related_name='user_order' ,on_delete=models.SET_NULL,null=True,blank=True)
    code = models.CharField(_("Code"), max_length=50, default=generate_code)
    status = models.CharField(_("Status"), max_length=1, choices=ORDER_STATUS)
    order_time = models.DateTimeField(_("Heure de Commande"), auto_now=True)
    delivery_time = models.DateTimeField(_("Heure d'expédition"), auto_now=False, auto_now_add=False,null=True,blank=True)


    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    

class OrderDetail(models.Model):
    ordre= models.ForeignKey(Order, verbose_name=_("Commande"),related_name='order_detail' ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Produit"), related_name='order_porduct' ,on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(_("Quantite"))
    price =models.FloatField(_("Prix"))
     

    def __str__(self):
        return str(self.ordre)

    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails' 