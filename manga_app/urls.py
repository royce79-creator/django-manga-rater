from django.urls import path
from .views import MangaListView, MangaDetailView

urlpatterns = [
  path('', MangaListView.as_view(), name='manga_list'),
  path('', MangaDetailView.as_view(), name='manga_list'),
]
