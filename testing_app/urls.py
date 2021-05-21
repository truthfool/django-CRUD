from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_details, name='postdetails'),
    path('create_user/', views.create_user, name='createuser'),
    path('userdetail/<int:id>/', views.user_details, name='userdetail'),
    path('updateuser/<int:id>/', views.update_user, name='updateuser'),
    path('deleteuser/<int:id>', views.delete_user, name='deleteuser')
]
