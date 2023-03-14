from .models import Cart, CartDetail


def panier(request):
    if request.user.is_authenticated:
        
        cart, created = Cart.objects.get_or_create(user= request.user , status = 'E')
        Cart_detail = CartDetail.objects.filter(cart = cart)
        return {'cart':cart , 'cart_detail':Cart_detail}
    else :
        return{}