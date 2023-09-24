import tweepy

api_key ='' # api key
api_secret ='' # api key secret
access_token ='' # access token 
access_token_secret ='' # access token secret
bearer_token = r''

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
auth.set_access_token(access_token, access_token_secret)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')
# Criar mensagem    
client.create_tweet(text=f'Olá mundo')
