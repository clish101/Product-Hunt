from django.urls import path, include
from . import views
from .views import createProductview, productDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='p-home'),
    path('create/', createProductview.as_view(), name='create-product'),
    path('vote/<int:vote_pk>/', views.votes, name='vote-cast'),
    path('product/<int:pk>/', productDetailView.as_view(), name='product-detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
