#5. Delete any student from table with their rollno.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    password='6393',
    user='postgres',
    port='5432'
)

create_table=""" create table student_4 (
    stu_roll int,
    stu_name varchar(200),
    stu_city varchar(200),
    stu_email varchar(200),
    primary key (stu_roll)
)
"""


print("table is created ")

insert_table='''insert into student_4 values 
(1,'amit','fatehpur','subhji7409@gmail.com'),
(2,'ankit','fatehpur','subhji7409@gmail.com'),
(3,'arjun','fatehpur','subhji7409@gmail.com')
 
    '''
cur=conn.cursor()    
cur.execute(insert_table)
conn.commit() 
print("table inserted")

delete_row='''delete  from student_4 where stu_roll =3'''

cur=conn.cursor()    
cur.execute(delete_row)
conn.commit() 

print("row is deleted from student table") 

