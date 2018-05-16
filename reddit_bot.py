import praw
import config
import time

# make list of all comments I've replied to
# add the id of the comm to the list
# make sure the comm id is not in the list

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "symbiosa's lucille bluth bot v0.1")
    print "Logged in"

    return r

def run_bot(r):
    print "Obtaining 50 comments..."

    comments_replied_to = []

    for comment in r.subreddit('NewBootGoofin').comments(limit=50):
        if "gene" in comment.body:
            print "string with \"gene\" found in comment " + comment.id
            #comment.reply("[AHH](https://i.imgur.com/1XmvM7G.gif)....Gene!")
            print "Replied to comment " + comment.id

            comments_replied_to.append(comment.id)

    print "Sleeping for 10 seconds..."
    #Sleep for 10 seconds...
    time.sleep(10)

    #list - way of storing data (very similar to an array)

r = bot_login()
while True:
    run_bot(r)
