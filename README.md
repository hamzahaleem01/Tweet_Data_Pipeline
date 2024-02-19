
# Data Pipeline in Dagster

This is a data pipeline using dagster as an ETL orchestration tool.

## Project Description

This data pipeline utilizes Dagster functionalities to retrieve tweet data through Twitter API calls and populate tables within a Postgresql database.

## Deployment

This pipeline is deployable both locally and within Docker containers. Execute the pipeline locally by running the dagster dev command in the terminal. Additionally, the code includes a docker-compose.yaml file for containerizing the pipeline and running it within Docker containers.

## Dependencies

A Postgresql database server is essential for this setup, as Dagster relies on it to store information regarding schedules, sensors, logs, etc. Additionally, data retrieved from the Twitter API is also loaded into the same Postgresql server but within a different database.

## Public Pypi
Python >= 3.10

| Package | Version | 
|---------|---------|
| asyncpg | 0.28.0 | 
| pandas | 2.1.1 | 
| sqlalchemy | 2.0.22 |
| dagster | 1.5.13 |
| dagster-webserver | 1.5.13 |
| dagster-postgres | 0.21.13 |
| dagit | 1.5.13 |
| greenlet | 3.0.3|
| tweepy | 4.14.0|

## Database Tables
**TableName:** tweets

| Column | Description | 
|---------|---------|
| twitter_user | Name of the twitter user | 
| date_created | Date and time the tweet was created | 
| number_of_likes | Number of likes the tweet received|
| source_of_tweet | Source of the tweet i.e. Web-App, iPhone, etc |
| tweet | content of the tweet in text format|

**TableName:** filters

| Column | Description | 
|---------|---------|
| filters | filter on which the developer wants to filter the tweets | 
| date_created | Date and time the filter was created | 
