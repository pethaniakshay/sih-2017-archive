import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from feature_extractor import *
import pickle


traintweet = training_set[:17000]
testtweet = training_set[17000:]
print 'train on %d instances, test on %d instances' % (len(traintweet), len(testtweet))
print 'training..........'
NBClassifier = nltk.NaiveBayesClassifier.train(traintweet)
cf = open("naivebayes1.pickle","wb")
pickle.dump(NBClassifier, cf)
cf.close()

print '-------------------------------------' 
print 'testing............'
print 'accuracy:', nltk.classify.util.accuracy(NBClassifier, testtweet)

