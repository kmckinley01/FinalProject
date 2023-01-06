import tweepy #library for accessing the Twitter API
import nltk #library for natural language processing
import textblob #library for sentiment analysis

#Put your Twitter API keys here
consumer_key = "EMb5s2N9YhLb6TUcKx7qmjyO9"
consumer_secret = "a4Z6y9ZSLOMNyvE6QoHLricW0RHsz7uDubnXTBMCd8ymCr7Jgh"
access_token = "1609208303338258432-uRyHxvN9oiEv6W06hSZAqfyIcowDnM"
access_token_secret = "aPhgQLAwCHzBPoqBueJdVUJg6hwC9VkBS6Xrzvi4TM0XH"
client = tweepy.Client(bearer_token=(access_token))

#Authenticate with the Twitter API using your API keys
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Create a Tweepy API client
api = tweepy.API(auth)

#List of six different politicians
politicians = ["Joe Biden", "Donald Trump", "Nancy Pelosi", "Mitch McConnell", "Bernie Sanders", "Elizabeth Warren"]

#Function to retrieve the top 50 tweets about a politician and run sentiment analysis on each tweet
def analyze_tweets(politician):
  #Get the top 50 tweets about the politician
  tweets = api.search_tweets(q=politician, count=50)

  #Initialize a list to store the sentiment scores of each tweet
  sentiment_scores = []

  #Loop through each tweet and calculate its sentiment score
  for tweet in tweets:
    #Get the text of the tweet
    tweet_text = tweet.text
    #Use TextBlob to perform sentiment analysis on the tweet
    sentiment = textblob.TextBlob(tweet_text).sentiment.polarity
    #Add the sentiment score to the list
    sentiment_scores.append(sentiment)

  #Calculate the average sentiment score of the tweets
  avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)

  #Print the average sentiment score
  print(f"The average sentiment score of the top 50 tweets about {politician} is {avg_sentiment}.")

#Print the names of the politicians
print("Choose a politician from the list:")
for politician in politicians:
  print(politician)

#Prompt the user to select a politician
selected_politician = input("Enter the name of the politician: ")

#Analyze the tweets about the selected politician
analyze_tweets(selected_politician)
