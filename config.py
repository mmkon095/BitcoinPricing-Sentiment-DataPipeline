apikey = "YOUR BINANCE API KEY"

secret = "YOUR BINANCE API SECRET"

twitapikey = "YOUR TWITTER API KEY"

twitapisec = "YOUR TWITTER API SECRET"

token = "YOUR API TOKEN"

tokensec = "YOUR API TOKEN SECRET"

aws_access_id = "YOUR AWS ACCESS ID"

aws_secret_acess = "YOUR AWS ACCESS SECRET"

upload_file_bucket = 'YOUR AWS S3 BUCKET'
upload_file_key = 'YOUR AWS S3 BUCKET FOLDER'

auth = tweepy.OAuthHandler(twitapikey,twitapisec)

auth.set_access_token(token,tokensec)

twitterapi = tweepy.API(auth, wait_on_rate_limit=True)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_words = "#bitcoin -filter:retweets"

today = datetime.date.today()
yesterday= today - datetime.timedelta(days=1)