import pickle
from feature_extractor import *
test = '"PJ_King","Loves twitter"'
loaded_model = pickle.load(open("naivebayes.pickle", 'rb'))
print "------------Positive------------"
print loaded_model.classify(extract_features(getFeatureVector(test)))
print "------------Negative------------"
test2 = "Morning everyone! In serious need of some decent coffee.. why isn't the catering open yet at 08.30?"
print loaded_model.classify(extract_features(getFeatureVector(test2)))