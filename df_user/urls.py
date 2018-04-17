from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register),
    path('register_handle/',views.register_handle),
    path('login/',views.login),
    path('login_handle/',views.login_handle),
    path('info/',views.info),
    path('register_exist/',views.register_exist),
    path('order/', views.order),
    path('site/', views.site),
    path('logout/', views.logout),
    path('user_center_order&<int:pageid>/', views.user_center_order),
]