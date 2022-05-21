from django.views.generic import ListView, DetailView
from .models import Manga

class MangaListView(ListView):
    template_name="manga_list.html"
    model = Manga

class MangaDetailView(DetailView):
    template_name="manga_detail.html"
    model = Manga
