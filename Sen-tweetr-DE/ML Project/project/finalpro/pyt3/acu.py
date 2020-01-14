import pickle
import nltk.classify
from acu1 import *

# Train the classifier
Classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Load")
print("Classifier accuracy percent:",(nltk.classify.accuracy(Classifier, test_set))*100)

