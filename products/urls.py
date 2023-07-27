"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import  views

app_name = 'products'

urlpatterns = [
    path('', views.products, name = 'index'),
    path('category/<int:category_id>', views.products, name = 'category'),
    path('page/<int:page_number>', views.products, name = 'paginator'),
    path('baskets/add/<int:product_id>', views.basket_add, name = 'basket_add'),
    path('baskets/remove/<int:id>', views.basket_remove, name = 'basket_remove'),
]

