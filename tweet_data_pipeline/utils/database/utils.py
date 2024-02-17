import pandas as pd
from sqlalchemy import insert

from tweet_data_pipeline.utils.database.connector import DBconnector
from tweet_data_pipeline.utils.database.orms import BaseType

from ... import logger


async def insert_base_orm_df(connector: DBconnector, base_orm: BaseType, df: pd.DataFrame) -> bool:  # type: ignore
    """Insert a given pandas dataframe based on a given ORM class.\
    Returns True if insert was successful, False otherwise."""
    if len(df.index) == 0:
        logger.debug(f"skipping insertion of of empty dataframe for orm: {base_orm}")
        insert_success = False
    else:
        async with connector.async_session_factory() as session:
            try:
                await session.execute(insert(base_orm), df.to_dict(orient="records"))  # type: ignore
            except Exception as e:
                e_msg = str(e).replace("\\n", " ")
                logger.error(
                    f"skipping insert on {base_orm.__tablename__},"
                    f"see error for more information (no DBAPIError): {e_msg}"
                )
                insert_success = False
            else:
                insert_success = True
            await session.commit()
    return insert_success
