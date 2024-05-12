from django.urls import path
from . import views
from .views import remove_from_cart
app_name = 'orders'

urlpatterns = [
    path('cart',views.CartView.as_view(), name = 'cart'),
    path('add-to-cart/<int:product_id>',views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]