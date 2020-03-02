import configparser
import psycopg2
from sql_queries-Copy1.py import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    
    """ This function loads Json data into staging_events and staging_songs from S3
    function arguements : Cursor and connection object
    
    
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()
        


def insert_tables(cur, conn):
    """
    This function loads data into star schema tables from stage tables
    following fact and dimension tables will be populated 
    
    Source Tables  ==>   Target Table
    staging_events , staging_songs  ===> songplays(fact table)
    Dim tables:
    staging_events ==> users,time
    staging_songs  ==> songs,artists
    
    
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ main functio to connect db and call loading stage and insert tables
    reads connection parameters from dwh config file
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()