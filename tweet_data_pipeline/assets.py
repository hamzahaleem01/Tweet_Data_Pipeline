from dagster import asset

from tweet_data_pipeline.twitter.tweets import getTweets

from . import connector, env_set


@asset
async def tweetInformation():
    """Wrapper fx to get tweets from twitter API and populate DB."""
    await getTweets(env_set, connector)
