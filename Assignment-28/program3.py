#3. Write a Select query to fetch all the students.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
    
)

create_table='''create table mobile_1 (
      mo_id int,
      mob_name varchar(100),
      mob_model varchar(200)
      )
      '''

print("table created ")

insert_value="""insert into mobile_1 values 
(1234,'Iphone_1', 'iphone 11 pro Max'),
(1235,'Iphone_2', 'iphone 12 pro Max'),
(1236,'Iphone_3', 'iphone 13 pro Max'),
(1237,'Iphone_4', 'iphone 14 pro Max')
"""
cur=conn.cursor()
cur.execute(insert_value)
conn.commit()
print("values inserted in table")



