from twython import Twython
import time

API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

twitter = Twython(API_KEY, API_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

while True:


    tweets = twitter.search(q='#駆け出しエンジニアと繋がりたい', lang='ja', result_type='recent', include_entities='false', count=1)
    tweets_length = len(tweets["statuses"])

    for i in range(tweets_length):

        tweet_name = tweets["statuses"][i]["user"]["name"]
        tweet_screen_name = tweets["statuses"][i]["user"]["screen_name"]
        tweet_text = tweets["statuses"][i]["text"]
        tweet_id = tweets["statuses"][i]["id"]
        print("name:{}\nscreen_name:{}\ntext:{}\nid:{}\n".format(tweet_name,tweet_screen_name,tweet_text,tweet_id))

        try:
            twitter.create_favorite(id=tweet_id)
            twitter.retweet(id=tweet_id)
            time.sleep(10)
        except:
            print("失敗しました")
            time.sleep(10)

    time.sleep(3600)
