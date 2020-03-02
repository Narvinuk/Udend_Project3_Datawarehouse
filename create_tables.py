import configparser
import psycopg2
from sql_queries1 import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """ This function drops exisiting tables from database
    Parameters : Cursor to connected db.
                 connection object
    
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Function creates tables ib db:
    following db tables will be created on sparkifydb
    songplays, users, artists, songs, time
    
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Create and connects to db
    drops existing tables and creates new tables.
    
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()