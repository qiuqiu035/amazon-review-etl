import pandas as pd
import snowflake.connector
from config import *

df = pd.read_csv('F:/amazon-review-etl/data/clean_reviews.csv')

conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

cs = conn.cursor()
cs.execute("""
CREATE OR REPLACE TABLE amazon_reviews(
    ProductId STRING,
    UserId STRING,
    ProfileName STRING,
    Score INT,
    Time DATE,
    Summary STRING,
    Text STRING,
    Review_length INT,
    Word_count INT    
);
""")


insert_sql = """
INSERT INTO amazon_reviews(
    ProductId, UserId, ProfileName, Score, Time, Summary, Text, Review_length, Word_count
) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

from snowflake.connector.pandas_tools import write_pandas
success, nchunks, nrows, _ = write_pandas(
    conn,
    df,
    table_name="AMAZON_REVIEWS",
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    auto_create_table=False,       
    quote_identifiers=False  
)
print(f"Uploaded {nrows} rows in {nchunks} batch(es). Success: {success}")

cs.close()
conn.close()

print("Data successfully inserted into Snowflake!")