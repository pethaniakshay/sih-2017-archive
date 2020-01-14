import pickle
from feature_extractor import *
test = '"PJ_King","Loves twitter"'
loaded_model = pickle.load(open("naivebayes.pickle", 'rb'))
print ("------------Positive------------")
print (loaded_model.classify(extract_features(getFeatureVector(test))))
print ("------------Negative------------")
test2 = '"Seth937","Fuck this economy. I hate aig and their non loan given asses."'
print (loaded_model.classify(extract_features(getFeatureVector(test2))))

