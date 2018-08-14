from django.urls import re_path, path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'products'
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]
