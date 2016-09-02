from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase

from classifier.views import index
from classifier.models import Category, Classifier, Sample


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_response = render(request, 'index.html')
        self.assertEqual(response.content.decode(), expected_response.content.decode())


def create_test_user():
    return User.objects.create_user('Jon', 'jon@test.com', 'jonpassword')

# def create_test_classifier():
#     first_classifier = Classifier()
#     first_classifier.user = user
#     first_classifier.name = 'First classifier'
#     first_classifier.save()


class ClassifierModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        user = create_test_user
        first_classifier = Classifier()
        first_classifier.user = user
        first_classifier.name = 'First classifier'
        first_classifier.save()

        second_classifier = Classifier()
        second_classifier.user = user
        second_classifier.name = 'Second classifier'
        second_classifier.save()

        saved_classifiers = Classifier.objects.all()
        self.assertEqual(saved_classifiers.count(), 2)

        first_saved_classifier = saved_classifiers[0]
        second_saved_classifier = saved_classifiers[1]
        self.assertEqual(first_saved_classifier.name, 'First classifier')
        self.assertEqual(second_saved_classifier.name, 'Second classifier')

    # def test_train_classifier(self):
    #     user = User.objects.create_user('Jon', 'jon@test.com', 'jonpassword')
    #     classifier = Classifier()
    #     classifier.user = user
    #     classifier.name = 'First classifier'
    #     classifier.save()
    #     category = Category()
    #     category.name = 'First category'
    #     category.save()
    #     sample = Sample()
    #     sample.category = category
    #     sample.classifier = classifier
    #     sample.text = 'First input sample'
    #     sample.save()


class CategoryModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        category = Category()
        category.name = 'First category'
        category.save()

        saved_categories = Category.objects.all()
        self.assertEqual(saved_categories.count(), 1)

        saved_category = saved_categories[0]
        self.assertEqual(saved_category.name, 'First category')


class SampleModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        user = User.objects.create_user('Jon', 'jon@test.com', 'jonpassword')
        classifier = Classifier()
        classifier.user = user
        classifier.name = 'First classifier'
        classifier.save()
        category = Category()
        category.name = 'First category'
        category.save()
        sample = Sample()
        sample.category = category
        sample.classifier = classifier
        sample.text = 'First input sample'
        sample.save()

        saved_samples = Sample.objects.all()
        self.assertEqual(saved_samples.count(), 1)

        saved_sample = saved_samples[0]
        self.assertEqual(saved_sample.text, 'First input sample')
