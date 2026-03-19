from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name='list'),
    path('create/', views.note_create, name='create'),
    path('edit/<int:pk>/', views.note_edit, name='edit'),
    path('delete/<int:pk>/', views.note_delete, name='delete'),
    path('<int:pk>/', views.note_detail, name='detail'),
]
