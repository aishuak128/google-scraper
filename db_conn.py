import psycopg2
from credentials import creds

# used "creds" dictionary from another .py file
conn = psycopg2.connect(user = creds['user'],
                password = creds['password'],
                host = creds['host'],
                port = creds['port'],
                database = creds['database'])

cursor = conn.cursor()

