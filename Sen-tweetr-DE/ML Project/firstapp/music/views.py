# Create your views here.
from django.http import HttpResponse
from django.template import loader
import tweepy
import json


access_token = '816618292219617280-fmH0nBMf9Jn8ZHmMAQZeCn3POLFPS1g'
access_token_secret = 'NMt4XexVeJxg0x7ChbmhpscwscJou2nP3SN63ol1ecqEH'
consumer_key = 'n5A5SfiNUuV6sklGZ9TSYuVoK'
consumer_secret = '0gygHMUJTzy1l0bOhZQZVInsUqQCoJZfPzLTpUejmAxauwJngY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.get_user('twitter')
name = user.screen_name
friends = user.friends()
# trend = api.trends_available()
search_results = api.search(q='sunny', count=10)
a = []


def index(request):
    abc = {'#Twitter', '#Amazon', '#Flipkart', '#netdlix', '#google'}
    template = loader.get_template('music/index.html')
    #query = request.GET.get("q")



    context = {
        'trends': trend(),
        'public_tweets': public_tweets,
        'search': search_results,
        'users': user,
        'names': name,
    }

    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('music/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def trend():
    raj = api.trends_place(2295404)
    for i in range(1, 10):
        a.append(raj[0]['trends'][i]['name'])
    return  a


def search(query):
    search_result = api.search(q=query, count=10)
    return search_result

