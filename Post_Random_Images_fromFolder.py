import os
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy

# Enter X API tokens below
bearer_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

# Absloute Path
script_dir = os.path.dirname(os.path.abspath(__file__))
#                                           ⬇️ The name of the folder
Image_directory = os.path.join(script_dir, "images")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

def SelectRandomImage():
    ImageFiles = os.listdir(Image_directory)
    if ImageFiles:
        RandomImage = random.choice(ImageFiles)
        ImagePath = os.path.join(Image_directory, RandomImage)
        return ImagePath

def PostImage():
    ImagePath = SelectRandomImage()
    media = api.media_upload(ImagePath)
    return media.media_id_string

def SendThePost():
    TextInThePost = "" # The text in the Tweet (Post)
    media_id = PostImage()
    client.create_tweet(text=TextInThePost, media_ids=[media_id])
    print(f"""
-----------------------------------------------------------------------
The Post has been sent!
Media ID : {media_id}
-----------------------------------------------------------------------

    """)


if __name__ == '__main__':
    # Initialize the scheduler
    scheduler = BlockingScheduler()

    # Schedule the job to run every minute (change to what do like)
    scheduler.add_job(SendThePost, 'interval', minutes=1)
    scheduler.start()


