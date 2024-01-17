from cmath import log
from tkinter import E 
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
from ecommapp.models import *
from accounts.models import Cart , CartItems
from django.http import HttpResponseRedirect
from ecommapp.views import add_to_cart



# from django.contrib import admin


# Create your views here.

def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request,"Account not found") 
            return HttpResponseRedirect(request.path_info)
        


        if user_obj[0].profile.is_email_verified:
            messages.warning(request,'Account is not verified.')
            return HttpResponseRedirect(request.path_info)


        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request,'Invalid Credentials')
        return HttpResponseRedirect(request.path_info)
    
    
    return render(request,'accounts/login.html')




def register_page(request):
    if request.method =='POST':
        full_name=request.POST.get("full_name")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user_obj=User.objects.filter(username=email)

        # user_obj=User.objects.create_user(full_name=full_name, email=email, password=password, username=email)
        # user_obj.set_password(password)
        # user_obj.save()

        # print(request.POST)

        # user_obj=User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, "Email is already registered.")
            return HttpResponseRedirect(request.path_info)
        
        # print(email)

        user_obj=User.objects.create( email=email, password=password, username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request,'An Email has been sent on your mail')
        return HttpResponseRedirect(request.path_info)

 # import django message to see whether user is registered or not

    
    return render(request,'accounts/register.html')
    


    # function for enable the email while verification

def activate_email(request, email_token):
    try:
        user=Profile.objects.get(email_token= email_token)
        user.is_email_verified=True
        user.save()
        return redirect('/')

    except Exception as e:
        return HttpResponse('Invalid Email token')



# def add_to_cart(request, slug):
#     # variant=request.GET.get('variant')
#     product = get_object_or_404(Product, slug=slug)
#     # product=Product.objects.get(slug=slug)
#     user=request.user
#     cart , _ = Cart.objects.get_or_create(user=user,is_paid=False)
#     cart_items,created=CartItems.objects.get_or_create(cart=cart,product=product)
#     if not created:
#         cart_items.quantity+=1
#         cart_items.save()

        
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def cart(request):
    try:
        cart = Cart.objects.get(is_paid=False, user=request.user.id)
        cart_items = cart.cart_items.all()

        context = {'cart': cart, 'cart_items': cart_items}
        return render(request, 'accounts/cart.html', context)

    except Cart.DoesNotExist:
        context = {'cart_items': []}
        return render(request, 'accounts/cart.html', context)













    # # context={'cart':}
    # # context={'cart': Cart.objects.get(is_paid=False , user=request.user)}
    # user_cart=Cart.objects.get(is_paid=False,user=request.user)
    # cart_items=user_cart.cart_items.all()
    # context = {
    #     'cart':user_cart,
    #     'cart_items':cart_items,
    # }
    # return render(request,'accounts/cart.html', context)


    