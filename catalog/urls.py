from django.urls import path
from catalog.apps import CatalogConfig
from .views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', products_list, name='products_list'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('newmodel/', NewModelListView.as_view(), name='newmodel_list'),
    path('newmodel/new/', NewModelCreateView.as_view(), name='newmodel_create'),
    path('newmodel/<int:pk>', NewModelDetailView.as_view(), name='newmodel_detail'),
    path('newmodel/<int:pk>/update/', NewModelUpdateView.as_view(), name='newmodel_update'),
    path('newmodel/<int:pk>/delete/', NewModelDeleteView.as_view(), name='newmodel_delete'),

]
