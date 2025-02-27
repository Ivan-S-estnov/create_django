from django.urls import path
from catalog.apps import CatalogConfig
from .views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),

    path('product/', ProductListView.as_view(), name='products_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('newmodel/', NewModelListView.as_view(), name='newmodel_list'),
    path('newmodel/new/', NewModelCreateView.as_view(), name='newmodel_create'),
    path('newmodel/<int:pk>', NewModelDetailView.as_view(), name='newmodel_detail'),
    path('newmodel/<int:pk>/update/', NewModelUpdateView.as_view(), name='newmodel_update'),
    path('newmodel/<int:pk>/delete/', NewModelDeleteView.as_view(), name='newmodel_delete'),

]
