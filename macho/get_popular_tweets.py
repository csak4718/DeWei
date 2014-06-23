import oauth2 as oauth
import urllib2 as urllib
import json, re
import csv,os

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="dr3dhFcvD2e04do2guz7jEu4E"
consumer_secret="4ggerCl2ow5eiE4yIeoAMd7FTeQ7ioyQYACVCLKEPdr8L6gKKM"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token_key="2465628674-gXdaKZsoh2Lcq4iIQ3HHTwobzw1Zstk4EW9pgVB"
access_token_secret="BGUaQOluefLl1edZQVqpMdIlgOKwwWYvcAr2uWg8ODmno"


_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  print url
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()# ??? line 413 at __init__.py
    #print url # the result is not the same as line 35

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data) # No problem. why not opener.urlopen()

  return response

def fetchsamples(key_word,until_date):
	# @ => %23f
	since_id='24012619984051000'
	max_id='250126199840518145'
	since_id_par="since_id=%(since_id)s"%{'since_id':since_id}
	max_id_par="max_id=%(max_id)s"%{'max_id':max_id}
	# result_type => mixed, recent, popular 
	result_type='mixed'
	result_type_par="result_type=%(result_type)s"%{'result_type':result_type}# catch the value(mixed) of key 'result_type'
	#print result_type_par # result_type=mixed
	count=100
	count_par="count=%(count)s"%{'count':count}
	until_par="until=%(until)s"%{'until':until_date}
	#&%(until_par)s
	lang='en'
	lang_par="lang=%(lang)s"%{'lang':lang}
	parameters="q=%(key_word)s&%(result_type_par)s&%(count_par)s&%(lang_par)s"%{'key_word':key_word,'result_type_par':result_type_par,'count_par':count_par,'until_par':until_par,'lang_par':lang_par}
	url = "https://api.twitter.com/1.1/search/tweets.json?%(parameters)s"%{'parameters':parameters}
	parameters = []
	response = twitterreq(url, http_method, parameters)
	#print response.read()
	retrieved_tweet_list=[]
	for result in response:
		twitter_response=json.loads(result)
		#print twitter_response['search_metadata']
		for tweet in twitter_response['statuses']:
			retrieved_tweet={}
			retrieved_tweet['screen_name']=tweet['user']['screen_name'].encode('utf-8')
			retrieved_tweet['id']=tweet['id']
			retrieved_tweet['text']=tweet['text'].encode('utf-8')
			retrieved_tweet['user_location']=tweet['user']['location'].encode('utf-8')
			retrieved_tweet['user_description']=tweet['user']['description'].encode('utf-8')
			retrieved_tweet['user_url']=tweet['user']['url']
			retrieved_tweet['created_at']=tweet['created_at'].encode('utf-8')
			retrieved_tweet['user_id']=tweet['user']['id']
			retrieved_tweet['followers_count']=tweet['user']['followers_count']
			retrieved_tweet['friends_count']=tweet['user']['friends_count']
			retrieved_tweet['listed_count']=tweet['user']['listed_count']
			retrieved_tweet['favourites_count']=tweet['user']['favourites_count']
			retrieved_tweet['retweet_count']=tweet['retweet_count']
			retrieved_tweet['favorite_count']=tweet['favorite_count']
			retrieved_tweet['user_lang']=tweet['user']['lang']
			retrieved_tweet_list.append(retrieved_tweet)
	'''
	print response
	for line in response:
		print line
		print line.strip()
	'''
	return retrieved_tweet_list # many {} in this []
if __name__ == '__main__':
	key_word='basketball'
	until_date='2014-05-04'
	tweet_list=fetchsamples(key_word,until_date)
	csv_file_name=os.path.join(os.getcwd(),'tweet_sample_popular.csv')
	with open(csv_file_name,'wb') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')
		csv_writer.writerow(['screen_name','id','text','user_location','user_description','user_url','created_at','user_id','followers_count','friends_count','listed_count','favourites_count','retweet_count','favorite_count','user_lang']) # write keys
		for tweet in tweet_list:
			print tweet # print every dictionary
			csv_writer.writerow([tweet['screen_name'],tweet['id'],tweet['text'],tweet['user_location'],tweet['user_description'],tweet['user_url'],tweet['created_at'],tweet['user_id'],tweet['followers_count'],tweet['friends_count'],tweet['listed_count'],tweet['favourites_count'],tweet['retweet_count'],tweet['favorite_count'],tweet['user_lang']]) # write values
