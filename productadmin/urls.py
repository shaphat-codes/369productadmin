
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import *
from rest_framework import routers
from products import views
from django.views.generic import TemplateView




file_router = routers.DefaultRouter()
file_router.register('file', views.ProductFileViewSet, basename='file')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('product-view/', ProductView, name="broadband-list"),
    path('product-create/', ProductCreate, name="product-create"),
    path('product-detail/<str:pk>', ProductDetail, name="product-detail"),
    path('product-update/<str:pk>', ProductUpdate, name="product-update"),



    path('product-import/', views.Product_Import, name="product-import"),
    path('product-clean/', views.ProductClean, name="product-clean"),
    path('file-upload/', include(file_router.urls)),
    path('file-delete/', views.DeleteProductFile, name="delete file"),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
