import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "symbiosa's lucille bluth bot v0.1")

    return r

def run_bot(r):
    for comment in r.subreddit('NewBootGoofin').comments(limit=50):
        if "gene" in comment.body:
            print "string found"
            comment.reply("AHH GENE PARMESAN")

r = bot_login()
run_bot(r)
