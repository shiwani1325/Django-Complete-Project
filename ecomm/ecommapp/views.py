from django.shortcuts import render, get_object_or_404
from ecommapp.models import Product
from accounts.models import Cart , CartItems
from django.http import HttpResponseRedirect


def get_product(request, slug):

    # print('*****')
    # print(request.user)
    # print('*****')
    try:
        # Use get_object_or_404 to handle the case where the product is not found
        # product = get_object_or_404(Product, slug=slug)
        product=Product.objects.get(slug=slug)
        context={'product': product}
        # return render(request, 'home/index.html', {'product': product})
        return render(request, 'ecommapp/index.html', context=context)

    except Exception as e:
        print(e)


def add_to_cart(request, slug):
    # variant=request.GET.get('variant')
    # product = get_object_or_404(Product, slug=slug)
    product=Product.objects.get(slug=slug)
    user=request.user
    cart , _ = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item = CartItems.objects.create(cart=cart,product=product,)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

