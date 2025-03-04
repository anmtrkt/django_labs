from django.urls import path

from . import views


urlpatterns= [
    path('', views.index, name='home'),
    path("create/", views.create, name='create'),
    path('edit/<uuid:id>/', views.edit, name='edit'),
    path('delete/<uuid:id>/', views.delete, name='delete'),
]