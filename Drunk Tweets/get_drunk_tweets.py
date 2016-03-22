import tweepy
import csv

CONSUMER_KEY = 'bVAzgkTVmARlIxRjmsNiSh5O0'
CONSUMER_SECRET = 'vr3NzU9JJVIKGSe1qDuV63ZbRZWA15mif8rh0dUaFxDDfTgV2Q'

ACCESS_TOKEN = '234065046-8dOvD31KuWHe242lkCnunzddxp7VvVe29uiVvtQO'
ACCESS_TOKEN_SECRET = 'B4uAEudjvcoLot5NZlF1wgMUviSJdItMKUS9Cy1pg7QvG'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#test stream
"""
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    def on_error(self, status_code):
        if status_code == 420:
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['drunk'])
"""

#test tweet
"""
tweet = api.get_status(id=461721857247694848)
info = [tweet.user.id_str, tweet.text, tweet.created_at,
        tweet.user.location, tweet.coordinates]
"""

#get ids and drunk identifiers
trainids=[]
drunk=[]
with open('../../../Downloads/icwsm-2016-data-release/alcohol-labeled-tweets-icwsm-2016-Q3.tsv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')
    for trainid,isdrunk in reader:
        trainids.append(trainid)
        drunk.append(isdrunk)




data = []
idlist = trainids
i = 0
for tweetid in idlist:
    if(drunk[i] == '1'):
        try:
            tweet = api.get_status(id=tweetid)
        except:
            pass
        try:
            user_id = tweet.user.id_str
        except:
            user_id = None
        try:
            text = tweet.text
        except:
            text = None
        try:
            datetime = tweet.created_at
        except:
            datetime = None
        try:
            coords = tweet.coordinates
        except:
            coords = None
        info = [user_id, tweetid, text, datetime,
                coords]
        if(info != []):
            data.append(info)
        i = i+1
    else:
        i = i+1


extended_data = data
for i in data:
    tweet = i
    datetime1 = i[3]
    newdrunktweets = []
    alltweets = []
    alltweets = api.user_timeline(user_id = tweet[0],count=200,since_id=tweet[1])
    alltweets.extend(new_tweets)
    uid = alltweets[-1]
    uid = uid.user.id
    uid = uid - 1
    success = False
    if alltweets[-1].created_at <= datetime1:
        for i in alltweets:
            if i.created_at > datetime1:
                if i.created_at < datetime1 + timedelta(hours=1):
                    newdrunktweets.extend(i)
                    print "~~added drunk tweet~~"
                    success = True
    while success == False:
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(user_id = tweet[0],count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
        print datetime1
        print alltweets[-1].created_at
        #sometimes it doesnt get back far enough
        #make it so it gives up if the oldest tweet is from the same date two iterations in a row
        if alltweets[-1].created_at <= datetime1:
            for i in alltweets:
                if i.created_at > datetime1:
                    if i.created_at < datetime1 + timedelta(hours=1):
                        newdrunktweets.extend(i)
                        print "~~  adding new drunk tweet to list  ~~"
                        success = True
