from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.show_new),
    path('shows/create', views.show_create),
    path('shows/<int:id>', views.show_show),
    path('shows/<int:id>/edit', views.show_edit),
    path('shows/<int:id>/update', views.show_update),
    path('shows/<int:id>/destroy', views.show_destroy)
]