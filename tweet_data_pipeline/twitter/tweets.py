import pandas as pd
import tweepy

import tweet_data_pipeline.utils.database.orms as orms
from tweet_data_pipeline.settings import Settings
from tweet_data_pipeline.utils.database.connector import DBconnector
from tweet_data_pipeline.utils.database.utils import (
    insert_base_orm_df,
    read_sql_query_to_list,
)
from sqlalchemy import select

from .. import logger


async def getTweets(env_set: Settings, connector: DBconnector) -> None:
    """Fetch tweets from twitter API and insert in database."""

    auth = tweepy.OAuth1UserHandler(
        env_set.CONSUMER_API_KEY,
        env_set.CONSUMER_API_KEY_SECRET,
        env_set.ACCESS_TOKEN,
        env_set.ACCESS_SECRET,
    )

    api = tweepy.API(auth, wait_on_rate_limit=True)

    filter_stmt = select(orms.Filters.filters)
    tweet_filters = await read_sql_query_to_list(connector, filter_stmt)

    search_query = (
        "'{}'".format("''".join([str(item[0]) for item in tweet_filters]))
        + "-filter:retweets AND -filter:replies AND -filter:links"
    )
    no_of_tweets = 100

    try:
        tweets = api.search_tweets(
            q=search_query, lang="en", count=no_of_tweets, tweet_mode="extended"
        )

        attributes_container = [
            [
                tweet.user.name,
                tweet.created_at,
                tweet.favorite_count,
                tweet.source,
                tweet.full_text,
            ]
            for tweet in tweets
        ]

        columns = [
            "User",
            "Date Created",
            "Number of Likes",
            "Source of Tweet",
            "Tweet",
        ]

        tweets_df = pd.DataFrame(attributes_container, columns=columns)
        await insert_base_orm_df(connector, orms.Tweets, tweets_df)

    except BaseException as e:
        logger.error("Status Failed On,", str(e))
