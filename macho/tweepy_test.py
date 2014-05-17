from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream # Why tweepy? Why not tweepy.streaming, like line 1.

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="dr3dhFcvD2e04do2guz7jEu4E"
consumer_secret="4ggerCl2ow5eiE4yIeoAMd7FTeQ7ioyQYACVCLKEPdr8L6gKKM"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2465628674-gXdaKZsoh2Lcq4iIQ3HHTwobzw1Zstk4EW9pgVB"
access_token_secret="BGUaQOluefLl1edZQVqpMdIlgOKwwWYvcAr2uWg8ODmno"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__': # if this .py is executed, it will execute this block.
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['baseball'])
    