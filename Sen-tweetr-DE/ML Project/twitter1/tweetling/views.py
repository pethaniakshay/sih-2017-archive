from django.http import HttpResponse
from django.template import loader
#from django.contrib.gis.utils import GeoIP
import tweepy

import pickle
#from feature_extractor import *
from tweetling.test import extract_features
from tweetling.test import getFeatureVector
import os


module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'stopwords.txt')

#import time
#import json

access_token = '816618292219617280-fmH0nBMf9Jn8ZHmMAQZeCn3POLFPS1g'
access_token_secret = 'NMt4XexVeJxg0x7ChbmhpscwscJou2nP3SN63ol1ecqEH'
consumer_key = 'n5A5SfiNUuV6sklGZ9TSYuVoK'
consumer_secret = '0gygHMUJTzy1l0bOhZQZVInsUqQCoJZfPzLTpUejmAxauwJngY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

module_dir3 = os.path.dirname(__file__)  # get current directory
file_path3 = os.path.join(module_dir3, "naivebayes.pickle")

loaded_model = pickle.load(open(file_path3, 'rb'))

api = tweepy.API(auth)
#g = GeoIP()
#x = g.city('72.14.207.99')

user = api.get_user('twitter')
name = user.screen_name
friends = user.friends()
#trend = api.trends_available()
res=""


def index(request):
    templates = loader.get_template('tweetling/index.html')
    client_ip = request.META['REMOTE_ADDR']
    context = {
        'trends': trend(),
        #'public_tweets': public_tweets,
        'search': search(request),
		'result':res,
        'users': user,
        'names': name,
        'pla':client_ip,
    }
    return HttpResponse(templates.render(context, request))


def about(request):
    template = loader.get_template('tweetling/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

# it give trending topic according rajkot
def trend():
    a = []
   
    raj = api.trends_place(2295404)
    for i in range(1, 10):
        a.append(raj[0]['trends'][i]['name'])
    return(a)
    """template = loader.get_template('tweetling/trending.html')
    raj = api.trends_place(2295404)
    for i in range(1, 10):
        a.append(raj[0]['trends'][i]['name'])
    context  {'a':a}
    return HttpResponse(template.render(context, request))
"""
def search(request):
	b = []
    # check the input methon type if get and 'q' is available then search functionslity will happen
    # else public tweet will display from home timeline
	if request.method == 'GET' and 'q' in request.GET:
            q = request.GET.get( 'q' )
            search_results = api.search(q , count=20)
            for i in search_results:
                b.append(loaded_model.classify(extract_features(getFeatureVector(i.text,file_path))))
                global res
                res=b
            return search_results
	else:
		public_tweets = api.home_timeline()
		return public_tweets
