import pickle
import os
from feature_extractor import extract_features,getFeatureVector


class first:
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'stopwords.txt')
    loaded_model = pickle.load(open("naivebayes.pickle", 'rb'))
    #test = '"PJ_King","Loves twitter"'
    #test2 = "Morning everyone! In serious need of some decent coffee.. why isn't the catering open yet at 08.30?"
    def function(self,test):
        print ("------------Positive------------")
        print (self.loaded_model.classify(extract_features(getFeatureVector(test,self.file_path))))
	
obj=first()
obj.function("good boy,i am to good to handle.but good is power full")