from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
#第1個django裡的測試-用django的resolve看開的網頁根目錄,是否是home_page
    def test_root_url_resolver_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
		
    def test_homepage_returns_correct_html(self):
	    request = HttpRequest()
	    response = home_page(request)
	    self.assertTrue(response.content.startswith(b'<html>'))
	    self.assertIn(b'<title>To-Do lists</title>', response.content)
	    self.assertTrue(response.content.endswith(b'</html>'))