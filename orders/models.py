from django.db import models

# Create your models here.
ORDER_STATUS = (
    ('R', 'Recieved'),
    ('C', 'Processed'),
    ('E', 'Shipped'),
    ('E', 'En cour'),
    

)


class Order(models.Model):
    pass


    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
