from django.db import models
from django.contrib.auth.models import User
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


class Classifier(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)

    def add_to_corpus():
        pass

    def train():
        pass

    def predict(self, text):
        X = []
        y = []
        bayes_pipe = Pipeline([('vectorizer', CountVectorizer()),
                               ('multinom', MultinomialNB())])
        corpus = self.sample_set.all()
        for sample in corpus:
            X.append(sample.text)
            y.append(sample.category.name)
        bayes_pipe.fit(X, y)
        y_pred = bayes_pipe.predict(text)

        return y_pred


class Category(models.Model):
    name = models.CharField(max_length=200)

class Sample(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category)
    classifier = models.ForeignKey(Classifier)
