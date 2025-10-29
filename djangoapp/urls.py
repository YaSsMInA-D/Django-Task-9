from django.urls import path
from . import views

app_name = "djangoapp"

urlpatterns = [
    path('', views.djangoapp_view, name='home'),  # url home page

    path('products/', views.product_list_view, name='product_list'),
    path('<slug:slug>/', views.person, name='person'),
    ]