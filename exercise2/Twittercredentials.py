import tweepy

consumer_key = "A3hs2Pdhzyhmn65W1oMeuySLM";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "IbNlP1VJH0bRVRZ0gAJWyperLrPRjPeObObxvypqvGg0R2e3S2";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "32722838-PcFSFcgKr1nae7TkwR2AoEpX7kfQqWxnqzyVQWYkL";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "YhhLqTuUYc6N8GLP2eqqTD4YCiyubOLWV5AYYaVH5bfK4";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



