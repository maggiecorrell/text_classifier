from django.db import models
from django.contrib.auth.models import User
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
import numpy as np
import pickle


class Classifier(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    pipeline = models.BinaryField(null=True, blank=True)

    def add_to_corpus():
        pass

    def train(self):
        X = []
        y = []
        pipeline = Pipeline([('vectorizer',
                              CountVectorizer(ngram_range=(1, 3))),
                            #  ('feature_selection',
                            #   VarianceThreshold(threshold=(.8*(1-.8)))),
                             ('multinom', MultinomialNB())])
        corpus = self.sample_set.all()
        for sample in corpus:
            X.append(sample.text)
            y.append(sample.category.name)
        X = np.array(X)
        y = np.array(y)
        self.pipeline = pickle.dumps(pipeline.fit(X, y))
        self.save()

    def predict(self, text):
        pipe = pickle.loads(self.pipeline)
        return pipe.predict(text)


class Category(models.Model):
    classifier = models.ForeignKey(Classifier)
    name = models.CharField(max_length=200)


class Sample(models.Model):
    text = models.TextField()
    classifier = models.ForeignKey(Classifier)
    category = models.ForeignKey(Category)

# class File_Upload(models.Model):
#     classifer = models.OneToOneField(Classifier)
#     text_body = models.TextField()
