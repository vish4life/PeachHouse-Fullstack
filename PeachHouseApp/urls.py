from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="main"),
    path('menu/',views.MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(),name='menuid'),
]