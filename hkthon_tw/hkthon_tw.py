from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as pd
import matplotlib as mpl

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import rcParams
from mpltools import style
from matplotlib import dates
from datetime import datetime
import seaborn as sns
import time 
import os 
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import random



#Seaborn plots
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
#ffplot
style.use('ggplot')
rcParams['axes.labelsize'] = 9
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 7
# rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = False
rcParams['figure.figsize'] = 20, 10

#Authentication
consumer_key = "QuJRNeZuIenUAPTW7NKtTNNRn"
consumer_secret = "qnDaMDdXthyvv9TjrbCGTzOSPnGOXVtd7GwyHhhjM6FF3d4yTe"
access_token = "844950851013820416-iVOK9onQgPM7AZdU0wA6ntKmdljjq4j"
access_token_secret = "iIsEpwCZnUwntR2QuIJk8A5gaiM8PfbcRIOrHAYKZ1a09"

MAX_TWEETS = 10
#This handles Twitter authentication and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth, wait_on_rate_limit=True)


#Data extraction
data = Cursor(api.search, q='#obama').items(MAX_TWEETS)

mozsprint_data = []
# You will use this line in production instead of this
# current_working_dir = os.path.dirname(os.path.realpath(__file__))
current_working_dir = "./"
log_tweets = current_working_dir  + 'moztweets.csv'
with open(log_tweets, 'w') as outfile:
	for tweet in data:
		mozsprint_data.append(json.loads(json.dumps(tweet._json)))
		outfile.write(json.dumps(tweet._json))
		outfile.write("\n")
		#print ("* ",mozsprint_data[0])  //unorganized data
		
# Create the dataframe we will use
tweets = pd.DataFrame()
# We want to know when a tweet was sent
tweets['created_at'] = str(map(lambda tweet: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), mozsprint_data))
# Who is the tweet owner
tweets['user'] = str(map(lambda tweet: tweet['user']['screen_name'], mozsprint_data))
# How many follower this user has
tweets['user_followers_count'] = map(lambda tweet: tweet['user']['followers_count'], mozsprint_data)
# What is the tweet's content
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), mozsprint_data)
# If available what is the language the tweet is written in
tweets['lang'] = map(lambda tweet: tweet['lang'], mozsprint_data)
# If available, where was the tweet sent from ?
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, mozsprint_data)
# How many times this tweet was retweeted and favorited
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], mozsprint_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], mozsprint_data)

y = tweets.head()
#print (type(y)) 
print ((tweets['text'].encode("utf-8"))
"""
new_tweets = str (tweets['text'].values)
original_tweets = 0
Retweets = 0
f = open('moztweets.csv')
for i in f:
	i = i.split(",")
	j = i[3]
	j = j[10:]
	#print (j)
	if j.startswith("RT"): original_tweets += 1
	else: Retweets += 1
	
print ("Number of Original Tweets : " , original_tweets)
print ("Number of Retweets : " , Retweets)
"""

# General plotting function for bar chart by language
"""//comment
:param category: Category plotted, can be tweets users, tweets language, tweets country etc ..
:param title: Title of the plot
:param x_title: List of the items in x
:param y_title: Title of the variable plotted
:return: a plot that we can save as pdf or png instead of displaying to the screen
//comment
"""
"""
def plot_tweets_per_category(category, title, x_title, y_title, top_n=5, output_filename="plot.png"):

	tweets_by_cat = category.value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x')
	ax.tick_params(axis='y')
	ax.set_xlabel(x_title)
	ax.set_ylabel(y_title)
	ax.set_title(title)
	tweets_by_cat[:top_n].plot(ax=ax, kind='bar')
	fig.savefig(output_filename)
	fig.show()
	

plot_tweets_per_category(tweets['lang'],"#obama by Language","Language","Number of Tweets", 5,"mozsprint_per_language.png")
plot_tweets_per_category(tweets['Location'],"#mozsprint by Location", "Location", "Number of Tweets", 5,"mozsprint_per_location.png")
plot_tweets_per_category(tweets['user'], "#mozsprint active users", "Users", "Number of Tweets", 5,"mozsprint_users.png")
"""