from .models import Cart, CartDetail


def panier(request):
    if request.user.is_authenticated:
        
        cart = Cart.objects.get_or_create(user= request.user , status = 'E')
        #Cart_detail = CartDetail.objects.filter()
        return {'cart':cart}