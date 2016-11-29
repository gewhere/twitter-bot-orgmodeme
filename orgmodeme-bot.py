import tweepy
import random

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('orgmodeme')

filename=open('/path/to/bot-data/data.txt','r')
f=filename.readlines()
filename.close()

num = len(f)
curr = random.randrange(1, num, 1)
print(curr)

if (curr%2 == 0):
    line = f[curr] + f[curr+1] + '#orgmode'
else:
    line = f[curr-1] + f[curr] + '#orgmode'

api.update_status(status=line)
