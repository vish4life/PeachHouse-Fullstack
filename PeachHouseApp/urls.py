from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('api/menu/',views.MenuItemViewAPI.as_view(),name='menuapi'),
    path('menu/',views.MenuItemView, name="menu"),
    # path('menu/<int:pk>',views.SingleMenuItemView.as_view(),name='menuid'),
]