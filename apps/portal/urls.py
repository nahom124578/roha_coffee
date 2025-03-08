from django.urls import path, include
from . import views

urlpatterns = [
    path('portal/', views.portal, name='portal'),
    path('portal/services/', views.service_list, name='service_list'),
    path('portal/services/new/', views.service_create, name='service_create'),
    path('portal/services/<int:pk>/', views.service_detail_update, name='service_detail'),
    path('portal/services/<int:pk>/edit/', views.service_detail_update, name='service_update'),
    path('portal/services/<int:pk>/delete/', views.service_delete, name='service_delete'),

]
