import praw
from textblob import TextBlob
import math

reddit = praw.Reddit(client_id='uifJuvRl06uxTg',
                     client_secret='Bf4eHDQhORvpJBw7syIvzat8gyA',
                     user_agent='subSentiment')

#Opens file with SubReddit Names
with open('subreddits.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())
        day_start = 1510635601
        day_end   = 1510721999

        sub_submissions = subreddit.stream.submissions()

        sub_sentiment   = 0
        num_comments    = 0

        for submission in sub_submissions:
            if not submission.stickied:
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                    blob = TextBlob(comment.body)

                    #adds comment sentiment to overall sentiment for subreddit
                    comment_sentiment =  blob.sentiment.polarity
                    sub_sentiment     += comment_sentiment
                    num_comments      += 1

        print('/r'+str(subreddit.display_name))
        try:
            print('Ratio: '+str(math.floor(sub_sentiment/num_comments*100))+'\n')
        except:
            print('No comment sentiment.'+'\n')
            ZeroDivisionError