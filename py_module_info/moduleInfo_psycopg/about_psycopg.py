'''
small demo to use psycopg lib (interact with postgres)

note: when script runs on same computer, 'localhost'

in order to set up for remote connection: 
* locations of postgresql.conf:
  * ~/<path_to>/postgres/postgresql.conf
  * ??
* if running on termux, change 'port' in conf to above 8000
* to connect remotely (another device), change 'listen_addresses' in conf to '*' or safer
* note: in termux: pg_ctl -D <path> restart





'''

import json
import psycopg as pg

if(__name__ == '__main__'):
    d = json.load(open('auth.json'))
    try:
        with pg.connect(
            host=d['host'],
            dbname=d['db'],
            user=d['user'],
            password=d['pass'],
            port=d['port']
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("select version();")
                db_version = cur.fetchone()
                print(f'ver: {db_version}')
    except pg.OperationalError as e:
        print(f'err {e}')


#eof

