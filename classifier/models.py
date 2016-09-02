from django.db import models
from django.contrib.auth.models import User


class Classifier(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)

    def add_to_corpus():
        pass

    def train():
        pass

    def predict():
        pass

class Category(models.Model):
    name = models.CharField(max_length=200)

class Sample(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category)
    classifier = models.ForeignKey(Classifier)
