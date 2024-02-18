from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path("items/new/", views.new_item, name='new_item'),
    path("items/<int:pk>", views.detail, name='detail'),

]