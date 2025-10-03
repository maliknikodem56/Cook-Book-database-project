"""
URL configuration for Cook_Book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.dishes_list, name='dishes_list'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('edit_dish/<int:dish_id>/', views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('add_cuisine/', views.add_cuisine, name='add_cuisine'),
    path('add_dish_type/', views.add_dish_type, name='add_dish_type'),
    path('add_diet/', views.add_diet, name='add_diet'),
    path('delete_cuisine/<int:cuisine_id>/', views.delete_cuisine, name='delete_cuisine'),
    path('delete_dish_type/<int:type_id>/', views.delete_dish_type, name='delete_dish_type'),
    path('delete_diet/<int:diet_id>/', views.delete_diet, name='delete_diet'),
]
