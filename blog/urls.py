from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_list_table', views.post_list_table, name='post_list_table'),
    path('post_list_json', views.post_list_json, name='post_list_json'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
