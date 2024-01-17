from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email
from ecommapp.models import Product

# Create your models here.
# to store user data/information
class Profile(BaseModel):
    full_name=models.CharField(max_length=150,default="")
    email=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=100,default="")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to="profile")

    # def __str__(self):
    #     return self.name

    def get_cart_count(self):
        return CartItems.objects.filter(cart_is_paid=False, cart_user=self.user).count()


class Cart(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE , related_name='carts')
    is_paid=models.BooleanField(default=False)

    def get_cart_total(self):
        cart_items=self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price)
        # print(price)
        return sum(price)


        # changes done by me 
    # def get_product_names(self):
    #     cart_items = self.cart_items.all()
    #     product_names = [cart_item.product_name for cart_item in cart_items]
    #     return product_names

    # def get_product_names(self):
    #     cart_items=self.cart_items.all()
    #     product_names=[]
    #     for cart_item in cart_items:
    #         product_names.append(cart_item.product.name)
    #     return product_names



class CartItems(BaseModel):
    cart=models.ForeignKey(Cart , on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank=True)
    # This change is done by me
    quantity=models.PositiveIntegerField(default=2)



    def get_product_price(self):
        price = [self.product.price]
        # this change is done by me
        # price=self.quantity*self.product.price
        return sum(price)

    # def get_product_names(self):
    #     product_names=[self.product_name]
    #     return product_names

    


    # def get_product_names(self):
    #     cart_items=self.cart_items.all()
    #     product_names=[]
    #     for cart_item in cart_items:
    #         product_names.append(cart_item.product.name)
    #     return product_names

     



@receiver(post_save,sender=User)
def send_email_token(sender,instance, created,**kwargs):
    try:
        if created:
            email_token=str(uuid.uuid4())
            Profile.objects.create(user=instance,email_token=email_token)
            email=instance.email
            # function in which we pass these.
            send_account_activation_email(email,email_token)
    except Exception as e:
        print(e)
