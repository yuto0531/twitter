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

        name = tweets["statuses"][i]["user"]["name"]
        screen_name = tweets["statuses"][i]["user"]["screen_name"]
        text = tweets["statuses"][i]["text"]
        user_id = tweets["statuses"][i]["id"]
        print("name:{}\nscreen_name:{}\ntext:{}\nid:{}\n".format(name,screen_name,text,user_id))

        try:
            twitter.create_favorite(id=user_id)
            twitter.retweet(id=user_id)
            time.sleep(10)
        except:
            print("失敗しました")
            time.sleep(10)

    time.sleep(3600)
