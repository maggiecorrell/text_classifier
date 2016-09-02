from django.db import models
from django.contrib.auth.models import User
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


class Classifier(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    pipeline = models.BinaryField(null=True, blank=True)

    def add_to_corpus():
        pass

    def train(self, user):
        X = []
        y = []
        self.pipeline = Pipeline([('vectorizer', CountVectorizer()),
                                  ('multinom', MultinomialNB())])
        corpus = self.sample_set.all()
        for sample in corpus:
            X.append(sample.text)
            y.append(sample.category.name)
        self.pipeline.fit(X, y)
        return

    def predict(self, text):
        y_pred = self.pipeline.predict(text)
        return y_pred


class Category(models.Model):
    name = models.CharField(max_length=200)

class Sample(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category)
    classifier = models.ForeignKey(Classifier)
