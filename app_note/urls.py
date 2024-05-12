from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('notes/<int:id>', views.notes_page, name='notes'),
    path('note/create/<int:owner_id>/', views.note_create, name='note_create'),
    path('note/<int:note_id>/,', views.note_page, name='note_form'),
    path('note/update/<int:note_id>/', views.note_update, name='note_update'),
    path('note/delete/<int:note_id>/', views.note_delete, name='note_delete'),
]