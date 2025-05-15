# Amazon Review ETL Pipeline Project

## Overview

This project demonstrates a full ETL (Extract, Transform, Load) data pipeline using customer review data from Amazon. The goal is to extract raw review data, clean and enrich it using Python, load it into a Snowflake cloud data warehouse, and run SQL-based analytical queries to uncover insights.

## Data Source

* **Dataset**: Amazon Fine Food Reviews
* **Records**: \~568,000
* **Fields**: ProductId, UserId, ProfileName, Score, Time, Summary, Text, etc.
* **Source**: [Kaggle - Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

## Tools & Technologies

* **Language**: Python (pandas, snowflake-connector)
* **Data Warehouse**: Snowflake
* **File Format**: CSV
* **Query Language**: SQL

## Pipeline Structure

```
Raw CSV File (Reviews.csv)
        ⬇
Python + Pandas (ETL scripts)
        ⬇
Cleaned DataFrame (df)
        ⬇
Snowflake (Table: amazon_reviews)
        ⬇
SQL Queries (Top products, rating stats)
        ⬇
CSV Export (for visualizations)
        ⬇
Upload to AWS S3
```

## Project Structure

```
amazon-review-etl/
├── data/
│ └── clean_reviews.csv
├── results/
│ ├── top_reviewed_products.csv
│ ├── top_rated_products.csv
│ ├── reviews_per_year.csv
│ ├── great_keyword_count.csv
│ ├── top_products_avg_reviewlength.csv
│ └── top_products_avg_wordcount.csv
├── scripts/
│   ├── extract_data.ipynb
│   ├── transform_data.ipynb
│   ├── load_to_snowflake.py
│   ├── upload_to_s3.py  
│   └── config.py 
├── docs/
│ └── etl_pipeline.png
└── README.md
```

## Example SQL Queries

```sql
-- Top 10 most reviewed products
SELECT ProductId, COUNT(*) AS review_counts
FROM amazon_reviews
GROUP BY ProductId
ORDER BY review_counts DESC
LIMIT 10;

-- Top 10 highest rated products (min 5 reviews)
SELECT ProductId, AVG(Score) AS avg_score
FROM amazon_reviews
GROUP BY ProductId
HAVING COUNT(*) > 5
ORDER BY avg_score DESC
LIMIT 10;

-- Yearly review volume
SELECT YEAR(Time) AS review_year, COUNT(*) AS total_reviews
FROM amazon_reviews
GROUP BY review_year
ORDER BY review_year;

-- Count of reviews containing "great"
SELECT COUNT(*) AS great_reviews
FROM amazon_reviews
WHERE Text ILIKE '%great%';

-- Top 10 products with longest average review length
SELECT ProductId, AVG(Review_length) AS avg_length
FROM amazon_reviews
GROUP BY ProductId
HAVING COUNT(*) > 5
ORDER BY avg_length DESC
LIMIT 10;

-- Top 10 products by average word count
SELECT ProductId, AVG(Word_count) AS avg_word_count
FROM amazon_reviews
GROUP BY ProductId
HAVING COUNT(*) > 5
ORDER BY avg_word_count DESC
LIMIT 10;
```

## Output Examples

* Top-reviewed product: `B007JFMH8M`
* Highest average score (5.0) with >5 reviews: `B003Z39VR2`
* Reviews containing "great": `138197` records
* Longest reviews by character length: `2224.8125`
* Longest reviews by word count: `406.6`

## Author

Hongyu Guo
ETL Project (2025)
Snowflake | Python | SQL
