
from django.urls import include,path
from accounts.views import login_page
from accounts.views import register_page
from accounts.views import activate_email
from ecommapp.views import add_to_cart
from accounts.views import cart
# from . import views



urlpatterns = [

    path('login/',login_page, name="login"),
    path('register/',register_page,name="register"),
    path('activate/<email_token>/',activate_email,name="activate_email"),
    path('cart/',cart, name="cart"),
    path('add_to_cart/<slug>/', add_to_cart, name="add_to_cart"),
    # path("ecommapp/", include("ecommapp.urls")),
    # path('admin/', admin.site.urls),
   
]