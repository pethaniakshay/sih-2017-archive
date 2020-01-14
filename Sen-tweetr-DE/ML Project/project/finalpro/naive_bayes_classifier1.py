import nltk.classify
import re, pickle, csv, os
import classifier_helper#, html_helper

#start class
class NaiveBayesClassifier:
	trainingDataFile = "full_training_dataset.csv"
	""" Naive Bayes Classifier """
    #variables    
    #start __init__
	#def __init__(self, data, keyword, time, trainingDataFile, classifierDumpFile, trainingRequired = 0):
	def __init__(self, trainingDataFile, classifierDumpFile, trainingRequired = 0):
		"""#Instantiate classifier helper        
		self.helper = classifier_helper.ClassifierHelper('feature_list.txt')
        
        self.lenTweets = len(data)
        self.origTweets = self.getUniqData(data)
        self.tweets = self.getProcessedTweets(self.origTweets)
        
        self.results = {}
        self.neut_count = [0] * self.lenTweets
        self.pos_count = [0] * self.lenTweets
        self.neg_count = [0] * self.lenTweets
        self.trainingDataFile = trainingDataFile

        self.time = time
        self.keyword = keyword
        self.html = html_helper.HTMLHelper()"""
        
        #call training model
		if(trainingRequired):
			self.classifier = self.getNBTrainedClassifer(trainingDataFile, classifierDumpFile)
		else:
			f1 = open(classifierDumpFile)            
			if(f1):
				self.classifier = pickle.load(f1)                
				f1.close()                
			else:
				self.classifier = self.getNBTrainedClassifer(trainingDataFile, classifierDumpFile)
    #end
	def getUniqData(self, data):
		uniq_data = {}        
		for i in data:
			d = data[i]
			u = []
			for element in d:
				if element not in u:
					u.append(element)
            #end inner loop
			uniq_data[i] = u            
        #end outer loop
		return uniq_data
    #end
	
	#start getProcessedTweets
	"""def getProcessedTweets(self, data):        
        tweets = {}        
        for i in data:
            d = data[i]
            tw = []
            for t in d:
                tw.append(self.helper.process_tweet(t))
            tweets[i] = tw            
        #end loop
        return tweets
    #end"""
	#start getNBTrainedClassifier
	def getNBTrainedClassifer(self, trainingDataFile, classifierDumpFile):        
		# read all tweets and labels
		tweetItems = self.getFilteredTrainingData(trainingDataFile)
        
		tweets = []
		for (words, sentiment) in tweetItems:
			words_filtered = [e.lower() for e in words.split() if(self.helper.is_ascii(e))]
			tweets.append((words_filtered, sentiment))
                    
		training_set = nltk.classify.apply_features(self.helper.extract_features, tweets)
		# Write back classifier and word features to a file
		classifier = nltk.NaiveBayesClassifier.train(training_set)
		outfile = open(classifierDumpFile, 'wb')        
		pickle.dump(classifier, outfile)        
		outfile.close()        
		return classifier
    #end