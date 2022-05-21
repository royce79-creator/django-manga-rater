from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from manga_app.models import Manga

class MangaTest(TestCase): 
  def setUp(self):
    self.user = get_user_model().objects.create_user(username = 'manga_joe', email='tester@email.com', password='pass')
    self.manga_app = Manga.objects.create(name = 'Naruto', rating = self.user, reviewer = 'Joe')

  def test_string_representation(self):
    self.assertEqual(str(self.snack), 'Joe')
  
  def test_snack_name(self):
    self.assertEqual(f'{self.snack.name}', 'Naruto')

  def test_list_page_status_code(self):
    url = reverse('manga_app')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  def test_list_page_template(self):
    url = reverse('manga_app')
    response = self.client.get(url)
    self.assertTemplateUsed(response,'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')
