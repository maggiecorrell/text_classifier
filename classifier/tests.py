from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from classifier.views import index


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_response = render(request, 'index.html')
        self.assertEqual(response.content.decode(), expected_response.content.decode())
