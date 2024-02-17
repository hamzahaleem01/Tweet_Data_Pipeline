from dagster import Definitions, load_assets_from_modules, get_dagster_logger
from tweet_data_pipeline.settings import Settings
from tweet_data_pipeline.utils.database.connector import DBconnector

logger = get_dagster_logger()
env_set = Settings()
connector = DBconnector(
    env_set.DB_HOST,
    env_set.DB_NAME,
    env_set.DB_USER,
    env_set.DB_PASSWORD,
    env_set.DB_PORT,
)


from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
