import praw
import random

reddit = praw.Reddit(
    client_id="Dhu5BDkroWpRBQ",
    client_secret="ojQeyIZ793E7I6fRFILOiLdJzdGNcg",
    user_agent="<console:WAFFLES:1.0>",
    username="yeWaffles",
    password="yeWaffles42"
)

subreddit = reddit.subreddit("waffles")

waffle_quotes = ['I have always loved Waffle House. It\'s been like an oasis in the desert many times late at night after one of my concerts. -Trace Adkins' ,
                    'Waffles are like pancakes with syrup traps. -Mitch Hedberg' ,
                    'You should eat a waffle! You can’t be sad if you eat a waffle! -Lauren Myracle',
                    'I don’t know about you, but I must fill every waffle square with syrup. -unknown',
                    'Waffles are pancakes with abs. -unknown',
                    'Life is too short to wonder where you hid your waffle maker. -Paula Deen']

for submission in subreddit.hot(limit=10):
    #print()
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " waffles " in comment_lower:
                print('->')
                print(comment.body)
                random_index = random.randint(0,len(waffle_quotes)-1)
                comment.reply(waffle_quotes[random_index])