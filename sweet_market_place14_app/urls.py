from django.urls import path
from .views import home_view, upload_product, ProductListView, product_detail

app_name = 'sweet_market_place14_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('upload_product/', upload_product, name='upload_product'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>/', product_detail, name='product'),

]
