from django.urls import path
from .views import KirimListView, KirimCreateView, KirimUpdateView, KirimDeleteView

urlpatterns = [
    path('kirimlar/', KirimListView.as_view(), name='kirim_page'),
    path('kirimlar/yaratish/', KirimCreateView.as_view(), name='kirim_create'),
    path('kirimlar/o\'zgartirish/<int:pk>/', KirimUpdateView.as_view(), name='kirim_update'),
    path('kirimlar/o\'chirish/<int:pk>/', KirimDeleteView.as_view(), name='kirim_delete'),
]