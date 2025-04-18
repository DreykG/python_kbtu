import psycopg2
#Connect to DataBase
connect = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="vlad19supkbtu",
    host="localhost",
    port="5432" 
)
cursor = connect.cursor()