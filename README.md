
# Data Pipeline in Dagster

This is a data pipeline using dagster as an ETL orchestration tool.

## Project Description

This data pipeline leverages the functionalities of Dagster to fetch tweets data from twitter API call and populate tables in the Postgresql database. 

## Deployment

This pipeline can be executed on local machine and on docker. Run `dagster dev` command in terminal to execute the pipeline locally. Moreover, the code also contains docker-compose.yaml file to containerize the pipeline and run on docker containers.

## Dependencies

Postgresql database server is needed as it is used by Dagster to store information related to schedules, sensors, logs, etc. Moreover, data from twitter API is also loaded in the same Postgresql server but difference database.

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
