from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wish/<int:product_id>/<slug:slug>/',
         views.wish_add_remove, name='wish_add_remove'),
    path('wishlist/',
         views.wish_list, name='wish_list'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
