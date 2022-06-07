# note: incomplete, work in progress ... 

import twint
import nest_asyncio
nest_asyncio.apply()
c = twint.Config()

text = input('Enter text to search for: ')   # text to search for in twitter
c.Search = text

username = input('Enter a specific username to look for or leave empty to skip: ')
if (username != ''):
    c.Username = username

c.Min_likes = input('Minimum number of likes: ')

c.Min_replies = input('Minimum number of replies: ')
c.Min_retweets = input('Minimum number of retweets: ')
c.Since = input('specify start date (YYYY-MM-DD): ')
c.Until = input('specify end date (YYYY-MM-DD): ')
lang = input('choose language (en - ar - ...) or leave empty for all: ')
if (lang != ''):
    c.Lang = lang
    
c.Limit = int(input('How many tweets would you like to see? '))

# use Pandas library
c.Pandas = True
# start searching
twint.run.Search(c)

def column_names():
    return twint.output.panda.Tweets_df.columns
def twint_to_pd(columns):
    return twint.output.panda.Tweets_df[columns]
column_names()

# you can add or remove any columns to your file from the previous available columns
tweet_df = twint_to_pd(["name","date", "tweet", "nlikes", "nreplies", "nretweets", "reply_to"])   # selected columns

tweet_df.head(10)
print(len(tweet_df))

#save dataset locally
tweet_df.to_csv( text + '.csv')