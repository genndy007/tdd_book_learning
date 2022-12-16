from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        res = self.client.get("/")
        html = res.content.decode("utf8")
        expected_html = render_to_string("home.html")

        self.assertTemplateUsed(res, "home.html")
        self.assertEqual(html, expected_html)
