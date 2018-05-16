import praw
import config
import time
import os

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "lucille bluth bot v0.1")
    print "Logged in"

    return r

def run_bot(r, comments_replied_to):
    print "Obtaining 50 comments..."


    for comment in r.subreddit('NewBootGoofin').comments(limit=50):
        if "gene" in comment.body and comment.id not in comments_replied_to and not comment.author != r.user.me():
            print "string with \"gene\" found in comment " + comment.id
            comment.reply("[AHH](https://i.imgur.com/1XmvM7G.gif)....Gene!")
            print "Replied to comment " + comment.id

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f: #a = append
                f.write(comment.id + "\n")

    print "Sleeping for 10 seconds..."
    time.sleep(10)

    #list - way of storing data (very similar to an array)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n") #every time the file has a new line it'll be split
            comments_replied_to = filter(None, comments_replied_to) # filter out the first arg from the 2nd arg

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to

while True:
    run_bot(r, comments_replied_to)
