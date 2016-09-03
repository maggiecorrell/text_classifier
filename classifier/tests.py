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


def create_test_classifier(user):
    classifier = Classifier()
    classifier.user = user
    classifier.name = 'First classifier'
    classifier.save()
    return classifier


def create_test_category(category_name):
    category = Category()
    category.name = category_name
    category.save()
    return category


def create_test_sample(classifier, category, text):
    sample = Sample()
    sample.category = category
    sample.classifier = classifier
    sample.text = text
    sample.save()
    return sample


class ClassifierModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        user = create_test_user()
        create_test_classifier(user)

        saved_classifiers = Classifier.objects.all()
        self.assertEqual(saved_classifiers.count(), 1)

        first_saved_classifier = saved_classifiers[0]
        self.assertEqual(first_saved_classifier.name, 'First classifier')

    def test_train_classifier(self):
        user = create_test_user()
        classifier = create_test_classifier(user)
        category1 = create_test_category('happy')
        category2 = create_test_category('sad')
        create_test_sample(classifier, category1, 'I feel happy today')
        create_test_sample(classifier, category1, 'I am happy for you')
        create_test_sample(classifier, category2, 'I feel sad today')
        create_test_sample(classifier, category2, 'How sad is that?')

        classifier.train()
        self.assertEqual(classifier.pipeline.predict(['I am happy']), ['happy'])


class CategoryModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        create_test_category('First category')

        saved_categories = Category.objects.all()
        self.assertEqual(saved_categories.count(), 1)

        saved_category = saved_categories[0]
        self.assertEqual(saved_category.name, 'First category')


class SampleModelTest(TestCase):
    def test_saving_and_retreiving_items(self):
        user = create_test_user()
        classifier = create_test_classifier(user)
        category = create_test_category('First category')
        create_test_sample(classifier, category, 'First input sample')

        saved_samples = Sample.objects.all()
        self.assertEqual(saved_samples.count(), 1)

        saved_sample = saved_samples[0]
        self.assertEqual(saved_sample.text, 'First input sample')
