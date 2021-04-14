import tweepy
import time
from dotenv import load_dotenv
import os
import random
import asyncio
import asyncpg
import threading
import backoff

kaisa_commands = ['kaisa', "kai'sa", 'kaikai', 'kai']
kaisa_text = ["That's me! :)", "Wanna go and dance a little bit?"]
ahri_commands = ['ahri', 'foxy', 'awi']
ahri_text = ['I love her so much!', "I haven't seen her all day I hope she is not overworking herself"]
evelynn_commands = ['evelynn', 'eviee', 'eve', 'evee', 'demon']
evelynn_text = ['EVIEEEE', 'Has she bought a new car again?', 'She is probably in the garage atm']
akali_commands = ['akali', 'kali', 'rouge']
akali_text = ['No Ramen now you had some yesterday', "Yes you'll get ramen today.", ]
sera_commands = ['seraphine', 'sera', 'seraboo']
sera_text = ['Protect her at all costs', "She's so cute I love her", "Hope she is not doing breaking anything again with Akali"]

like_texts = ['#Kaisa', '#KAISA', "#Kai'sa", "#Kai'Sa", "#KAI'SA", "#kai'sa"]

load_dotenv()
consumer_key: str = os.getenv('consumer_key')
consumer_secret: str = os.getenv('consumer_secret')
access_token: str = os.getenv('access_token')
access_token_secret: str = os.getenv('access_token_secret')


async def main():
    conn = await asyncpg.create_pool(user=os.getenv('DB_USER'), password=os.getenv('DB_PW'),
                                     database=os.getenv('DB_NAME'), host=os.getenv('DB_HOST'),
                                     port=os.getenv('DB_PORT'))

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # upload_image(api, "test.png")
    # send_image(api, [1381959863958396938])
    while True:
        status = api.rate_limit_status()
        #print(api.rate_limit_status())
        print(status['resources']['followers']['/followers/ids'])
        print(status['resources']['statuses']['/statuses/user_timeline'])
        print(status['resources']['statuses']['/statuses/mentions_timeline'])
        print(status['resources']['friends']['/friends/list'])
        mentions = get_mentions(api)
        await command_handler(api, conn, mentions)
        follow_back(api)
        await auto_like(api, conn)
        await auto_retweet(api, conn)

        await asyncio.sleep(240)
    # print(mentions)


@backoff.on_exception(backoff.expo, tweepy.TweepError, max_tries=8)
def follow_back(api):
    try:
        followers = api.followers_ids()
        following = api.friends()
        for follower in followers:
            if follower not in following:
                api.create_friendship(user_id=follower)
    except Exception as err:
        print(err)


@backoff.on_exception(backoff.expo, tweepy.TweepError, max_tries=8)
async def auto_like(api, db):
    try:
        following = api.friends()
        for follow in following:
            tweets = api.user_timeline(user_id=follow.id, exclude_replies=True)
            for tweet in tweets:
                like = await db.fetch(
                    """
                    SELECT * FROM liked WHERE tweet_id = $1
                    """, tweet.id
                )
                if not like:
                    if any(like_text in tweet.text for like_text in like_texts):
                        try:
                            api.create_favorite(tweet.id)
                            await db.execute(
                                """
                                INSERT INTO liked VALUES ($1)
                                """, tweet.id
                            )
                        except Exception as err:
                            print(err)
        following.clear()
    except Exception as err:
        print(err)


@backoff.on_exception(backoff.expo, tweepy.TweepError, max_tries=8)
async def auto_retweet(api, db):
    try:
        following = api.friends()
        for follow in following:
            tweets = api.user_timeline(user_id=follow.id, exclude_replies=True, include_rts=False)
            for tweet in tweets:
                like = await db.fetch(
                    """
                    SELECT * FROM retweeted WHERE tweet_id = $1
                    """, tweet.id
                )
                if not like:
                    if any(like_text in tweet.text for like_text in like_texts):
                        if 'media' in tweet.entities.keys():
                            try:
                                api.retweet(tweet.id)
                                await db.execute(
                                    """
                                        INSERT INTO retweeted VALUES ($1)
                                        """, tweet.id
                                )
                            except Exception as err:
                                print(err)
        following.clear()
    except Exception as err:
        print(err)


@backoff.on_exception(backoff.expo, tweepy.TweepError, max_tries=8)
async def command_handler(api, db, mentions):
    for mention in mentions:
        reply = await db.fetch(
            """
            SELECT * FROM replied WHERE tweet_id = $1
            """, mention.id
        )
        if not reply:
            valid = False
            try:
                command = (mention.text.split('!'))[1]
                if command.lower() in kaisa_commands:
                    api.update_status(status=random.choice(kaisa_text), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
                    valid = True
                elif command.lower() in akali_commands:
                    api.update_status(status=random.choice(akali_text), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
                    valid = True
                elif command.lower() in ahri_commands:
                    api.update_status(status=random.choice(ahri_text), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
                    valid = True
                elif command.lower() in evelynn_commands:
                    api.update_status(status=random.choice(evelynn_text), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
                    valid = True
                elif command.lower() in sera_commands:
                    api.update_status(status=random.choice(sera_text), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
                    valid = True

                if valid:
                    await db.execute(
                        """
                        INSERT INTO replied VALUES ($1)
                        """, mention.id
                    )

                # print(command)
            except Exception as err:
                # print(err)
                pass


@backoff.on_exception(backoff.expo, tweepy.TweepError, max_tries=8)
def get_mentions(api):
    try:
        replies = api.mentions_timeline()
    except Exception as err:
        print(err)
    return replies


def send_image(api, image_id):
    api.update_status(media_ids=image_id)
    return


def upload_image(api, image_name):
    media = api.media_upload(filename=image_name)

    uploaded = False

    while not True:
        response = api.get_media_upload_status(media.media_id)
        time.sleep(0.5)


if __name__ == "__main__":
    print('start {}'.format(time.time()))
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())  # run foo 5 times
    loop.run_forever()
    print('finish {}'.format(time.time()))
    print('done')
    loop.close()
