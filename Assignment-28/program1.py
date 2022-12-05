#1. Create a table (student) with 3 columns (rollno, name, course).



import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
)


creat_query= '''create table student (
     stu_roll_no int , 
     stu_name varchar(200), 
     stu_course varchar(200))
     '''



cur=conn.cursor()
cur.execute(creat_query)
conn.commit()
print("table successful created")




