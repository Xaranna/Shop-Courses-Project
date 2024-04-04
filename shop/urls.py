from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course,  name='single_course'),
    path('cart/add/<int:course_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
]