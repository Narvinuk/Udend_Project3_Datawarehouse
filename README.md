Project Description:

The objective of this project is to create cloud data warehouse for a music streaming startup, Sparkify from Json files to help Sparkify analyze their user activity 
and  what users are listening and which songs.

Source data set in Json format on AWS S3 storage in two files
Song-data and log_data

Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song.

Log Dataset:
This is an event data set generated based on user activity
stores user activity like what songs they are listening to and user ,artist information.

Below is the process flow for this project:

Connect to AWS Redshift
Create Sparkify db
Drop existing tables
Create Stage tables
Create fact table
Create Dim tables
Load Stage table
Load Fact and Dim tables.

Process execution steps:

This project contains 3 python scripts 
Sql_queries.py
Create_tables.py
etl.py

Sql_queries.py

	This scripts contains Drop, Create and Insert statements which will be used in
           Create_tables.py and etl.py as an import.

Run Create_tables.py from console :
This script imports  table definitions from sql_queries.py  to drop and create tables on    sparkify db.



Following tables will be created after execution
Staging table:

“staging_events"
“Staging_songs"

Fact Table: 
“Songplay"  -- This Fact table contains what songs user are listening  and provide data for analytics 

Dimesnsion Tables:

“users"  -- This Dimension table contains Users information like user id ,name
“songs"  --This Dimension table contains Songs information like song id,title
“artists" -- This Dimension table contains artist information like artist name and locaiton
“time" -- This is a derived dimension table contains date and time information.
Output : Creates tables on database

Run etl.py  from Console:

This is an ETL scripts which loads the data from Json files to target tables:

Executes Copy command to copy data from Json files to Stage tables
Then inserts data from stage tables into Fact and Dimension tables.

Output : Tables will be populated with data




