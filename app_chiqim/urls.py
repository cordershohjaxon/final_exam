from django.urls import path
from .views import ChiqimListView, ChiqimCreateView, ChiqimUpdateView, ChiqimDeleteView

urlpatterns = [
    path('chiqimlar/', ChiqimListView.as_view(), name='chiqim_page'),
    path('chiqimlar/yaratish/', ChiqimCreateView.as_view(), name='chiqim_create'),
    path('chiqimlar/yangilash/<int:pk>/', ChiqimUpdateView.as_view(), name='chiqim_update'),
    path('chiqimlar/o\'chirish/<int:pk>/', ChiqimDeleteView.as_view(), name='chiqim_delete')
]