from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

'''
Product Models
Aut : Chatouirabie@gmail.com

'''
FLAG_CHOICE = (
    ('N','Nouveau'),
    ('V','Produit Vedette'),
    ('P','Promo'),
)

class Product(models.Model):

    nom = models.CharField(_("Nom"),max_length=100)
    image = models.ImageField(_("Image"), upload_to='products')
    prix = models.FloatField(_("Prix"))
    sku = models.IntegerField(_("SKU"))
    subtitle = models.CharField(_("SousTitre"), max_length=350)
    description = models.TextField(_("Description"), max_length=30000)
    flag = models.CharField(_("Flag"), max_length=1,choices=FLAG_CHOICE)
    slug =  models.SlugField(_("Slug"), null=True,blank=True)
    brand =  models.ForeignKey("Brand", verbose_name=_("Brand"),related_name='productbrand', on_delete=models.SET_NULL, null=True,blank=True)
    tags= TaggableManager()

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.nom
    
class Brand(models.Model):
    non = models.CharField(_("Nom"),max_length=50)
    image =  models.ImageField(_("Image"), upload_to='brands')
    slug = models.SlugField(_("Slug"))

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.nom

class ProductImages(models.Model):
    product =models.ForeignKey(Product, verbose_name=_("Product"), related_name='productimage',on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product_Images')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
    

    def __str__(self):
        return str(self.product)
    
class ProductReview(models.Model):
    user= models.ForeignKey(User, verbose_name=_("User"), related_name='reviewuser', on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='productreview', on_delete=models.CASCADE)
    rate =models.IntegerField(_("Rate"), max_length=1)
    review = models.TextField(_("Review"), max_length=1000)
    date = models.DateTimeField(_("Date"), auto_now=True)
    
    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return str(self.product) 
